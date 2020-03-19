from Algorithm import Axiom, FitnessTest, Test
from Runner import Runner


class MaxConnectionsAxiom(Axiom):
    def __init__(self, max):
        self.max = max

    def isValid(self, graph):
        return len(graph.connections) <= self.max


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
