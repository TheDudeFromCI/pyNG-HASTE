from Algorithm import DataType, Function, Node, Connection, NodeGraph, GraphContainer
from Algorithm import Environment, Axiom, Heuristic, Test, FitnessTest, SearchTree


class NumberDataType(DataType):
    def connectsTo(self, dataType):
        return isinstance(dataType, NumberDataType)


class OutputNumberFunction(Function):
    def __init__(self):
        super().__init__([NumberDataType()], [])

    def run(self):
        pass


class AddFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self):
        pass


class InputNumberFunction(Function):
    def __init__(self):
        super().__init__([], [NumberDataType()])

    def run(self):
        pass


class MaxConnectionsAxiom(Axiom):
    def __init__(self, max):
        self.max = max

    def isValid(self, graph):
        return len(graph.connections) <= self.max


if __name__ == '__main__':
    graph = NodeGraph()
    graph.addNode(OutputNumberFunction())

    container = GraphContainer()
    container.push(graph)

    env = Environment()
    env.addAxiom(MaxConnectionsAxiom(3))
    env.addFunction(AddFunction())
    env.addFunction(InputNumberFunction())

    tree = SearchTree(container, env)

    print('Running...')
    iterations = 0
    while not container.isEmpty():
        tree.nextItr()
        iterations += 1

    print('Finished in', iterations, 'iterations.')

    print('Solutions: ({})\n\n'.format(len(tree.solutions)))
    for solution in tree.solutions:
        print(solution, '\n')
