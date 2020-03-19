class DataType:
    def connectsTo(self, dataType):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class Function:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def run(self, inputs):
        raise NotImplementedError


class Node:
    def __init__(self, function, index):
        self.function = function
        self.index = index

    def __str__(self):
        inputs = ''
        outputs = ''

        for dataType in self.function.inputs:
            if inputs:
                inputs += ', '

            inputs += str(dataType)

        for dataType in self.function.outputs:
            if outputs:
                outputs += ', '

            outputs += str(dataType)

        return '{}({}) -> ({})'.format(self.function.__class__.__name__, inputs, outputs)


class Connection:
    def __init__(self, outputNode, outputPlug, inputNode, inputPlug):
        self.outputNode = outputNode
        self.outputPlug = outputPlug
        self.inputNode = inputNode
        self.inputPlug = inputPlug


class NodeGraph:
    def __init__(self):
        self.nodes = []
        self.connections = []
        self.heuristic = 0
        self.fitness = 0

    def addNode(self, function):
        node = Node(function, len(self.nodes))
        self.nodes.append(node)

        return node

    def addConnection(self, connection):
        self.connections.append(connection)

    def copy(self):
        graph = NodeGraph()

        for node in self.nodes:
            graph.nodes.append(Node(node.function, node.index))

        for conn in self.connections:
            outputNode = graph.nodes[conn.outputNode.index]
            inputNode = graph.nodes[conn.inputNode.index]

            graph.connections.append(Connection(
                outputNode, conn.outputPlug, inputNode, conn.inputPlug))

        return graph

    def __str__(self):
        if self.isSolution():
            s = 'Graph: (Solution, Fitness: {:.1f})'.format(self.fitness)
        else:
            s = 'Graph: (Heuristic: {:.1f}'.format(self.heuristic)

        for index, node in enumerate(self.nodes):
            s += '\n  {}) {}'.format(index, node)

        for index, conn in enumerate(self.connections):
            s += '\n  {}:{} => {}:{}'.format(conn.outputNode.index,
                                             conn.outputPlug, conn.inputNode.index, conn.inputPlug)

        return s

    def getConnectionTo(self, node, plugIndex):
        for conn in self.connections:
            if conn.inputNode is node and conn.inputPlug == plugIndex:
                return conn

        return None

    def getConnectionsFrom(self, node, plugIndex):
        conns = []

        for conn in self.connections:
            if conn.outputNode is node and conn.outputPlug == plugIndex:
                conns.append(conn)

        return conns

    def nextOpenPlug(self):
        for node in reversed(self.nodes):
            for plug in range(len(node.function.inputs)):
                conn = self.getConnectionTo(node, plug)

                if conn is None:
                    return (node, plug)

        return None

    def isSolution(self):
        return self.nextOpenPlug() is None

    def childGraphs(self, env):
        children = []

        node, plug = self.nextOpenPlug()
        dataType = node.function.inputs[plug]

        for function in env.functions:
            for outputPlugIndex, outputPlug in enumerate(function.outputs):
                if outputPlug.connectsTo(dataType):
                    child = self.copy()

                    newNode = child.addNode(function)
                    oldNode = child.nodes[node.index]
                    conn = Connection(newNode, outputPlugIndex, oldNode, plug)

                    child.addConnection(conn)
                    children.append(child)

        for sibNode in self.nodes:
            if self.isParentOf(node, sibNode):
                continue

            for outputPlugIndex, outputPlug in enumerate(sibNode.function.outputs):
                if outputPlug.connectsTo(dataType):
                    child = self.copy()

                    newNode = child.nodes[sibNode.index]
                    oldNode = child.nodes[node.index]
                    conn = Connection(newNode, outputPlugIndex, oldNode, plug)

                    child.addConnection(conn)
                    children.append(child)

        return children

    def isParentOf(self, parentNode, childNode):
        if parentNode is childNode:
            return True

        for conn in self.connections:
            if conn.outputNode is parentNode:
                if self.isParentOf(conn.inputNode, childNode):
                    return True

        return False


class GraphContainer:
    def __init__(self):
        self.graphs = []
        self.solutions = []

    def isEmpty(self):
        return len(self.graphs) == 0

    def pull(self):
        if self.isEmpty():
            raise RuntimeError

        return self.graphs.pop()

    def push(self, graph):
        self.graphs.append(graph)
        self.graphs.sort(key=lambda g: g.heuristic)

    def addSolution(self, graph):
        self.solutions.append(graph)
        self.graphs.sort(key=lambda g: g.fitness, reverse=True)


class Axiom:
    def isValid(self, graph):
        raise NotImplementedError


class Heuristic:
    def getValue(self, graph):
        raise NotImplementedError


class Test:
    def isValid(self, graph):
        raise NotImplementedError


class FitnessTest:
    def getValue(self, graph):
        raise NotImplementedError


class Environment:
    def __init__(self):
        self.axioms = []
        self.heuristics = []
        self.tests = []
        self.fitnessTests = []
        self.functions = []

    def addAxiom(self, axiom):
        self.axioms.append(axiom)

    def addHeuristic(self, heuristic):
        self.heuristics.append(heuristic)

    def addTest(self, test):
        self.tests.append(test)

    def addFitnessTest(self, fitnessTest):
        self.fitnessTests.append(fitnessTest)

    def addFunction(self, function):
        self.functions.append(function)


class SearchTree:
    def __init__(self, container, env):
        self.container = container
        self.env = env

    def nextItr(self):
        graph = self.container.pull()

        for child in graph.childGraphs(self.env):
            valid = True
            for axiom in self.env.axioms:
                if not axiom.isValid(child):
                    valid = False
                    break

            if not valid:
                continue

            if child.isSolution():
                for test in self.env.tests:
                    if not test.isValid(child):
                        valid = False
                        break

                if not valid:
                    continue

                child.fitness = 0
                for fitnessTest in self.env.fitnessTests:
                    child.fitness += fitnessTest.getValue(child)

                self.container.addSolution(child)
            else:
                child.heuristic = 0
                for heuristic in self.env.heuristics:
                    child.heuristic += heuristic.getValue(child)

                self.container.push(child)


def buildGraph(inputs, output):
    graph = NodeGraph()
    graph.addNode(output)

    for input in inputs:
        graph.addNode(input)

    return graph
