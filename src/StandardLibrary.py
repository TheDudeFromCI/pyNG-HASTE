import random
from Algorithm import Axiom, FitnessTest, Test, DataType, Function, Heuristic
from Runner import Runner


class NumberDataType(DataType):
    def connectsTo(self, dataType):
        return isinstance(dataType, NumberDataType)


class IntegerDataType(DataType):
    def connectsTo(self, dataType):
        return isinstance(dataType, NumberDataType) \
            or isinstance(dataType, IntegerDataType)


class BoolDataType(DataType):
    def connectsTo(self, dataType):
        return isinstance(dataType, BoolDataType)


class MaxConnectionsAxiom(Axiom):
    def __init__(self, max):
        self.max = max

    def isValid(self, graph):
        inputPlugs = 0
        for node in graph.nodes:
            inputPlugs += len(node.function.inputs)

        return inputPlugs <= self.max


class FewerConnectionsFitness(FitnessTest):
    def __init__(self, magnitude=1):
        self.magnitude = magnitude

    def getValue(self, graph):
        return len(graph.connections) * -self.magnitude


class InputOutputTest(Test):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def isValid(self, graph):
        try:
            runner = Runner(graph)
            results = runner.findValues(self.inputs)

            return results == self.outputs
        except:
            return False


class AllInputsUsedTest(Test):
    def __init__(self, inputCount):
        self.inputCount = inputCount

    def isValid(self, graph):
        for i in range(self.inputCount):
            if len(graph.getConnectionsFrom(graph.nodes[i + 1], 0)) == 0:
                return False

        return True


class IfFunction(Function):
    def __init__(self, dataType):
        super().__init__([BoolDataType(), dataType, dataType], [dataType])

    def run(self, inputs):
        if inputs[0]:
            return [inputs[1]]
        else:
            return [inputs[2]]


class InputBoolFunction(Function):
    def __init__(self):
        super().__init__([], [BoolDataType()])

    def run(self, inputs):
        pass


class OutputNumberFunction(Function):
    def __init__(self):
        super().__init__([NumberDataType()], [])

    def run(self, inputs):
        pass


class OutputIntegerFunction(Function):
    def __init__(self):
        super().__init__([IntegerDataType()], [])

    def run(self, inputs):
        pass


class InputNumberFunction(Function):
    def __init__(self):
        super().__init__([], [NumberDataType()])

    def run(self, inputs):
        pass


class InputIntegerFunction(Function):
    def __init__(self):
        super().__init__([], [IntegerDataType()])

    def run(self, inputs):
        pass


class PreferSmallerHeuristic(Heuristic):
    def __init__(self, magnitude=0.1):
        self.magnitude = magnitude

    def getValue(self, graph):
        return len(graph.connections) * -self.magnitude


class RandomHeuristic(Heuristic):
    def __init__(self, magnitude=1.0):
        self.magnitude = magnitude * 2

    def getValue(self, graph):
        return random.random() - self.magnitude


class UnlikelyFunctionHeuristic(Heuristic):
    def __init__(self, function, magnitude=100.0):
        self.function = function
        self.magnitude = magnitude

    def getValue(self, graph):
        for node in graph.nodes:
            if node.function == self.function:
                return -self.magnitude

        return 0


class CheckForErrorsAxiom(Axiom):
    def __init__(self, tests):
        self.tests = tests

    def isValid(self, graph):
        try:
            runner = Runner(graph)
            for test in self.tests:
                runner.findValues(test)
            return True
        except:
            return False
