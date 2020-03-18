from Algorithm import Axiom, FitnessTest


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
