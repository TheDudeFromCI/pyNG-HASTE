class BranchingFactor:
    def __init__(self):
        self.branches = {}

    def addSample(self, connections, children):
        if connections in self.branches:
            samples, total = self.branches[connections]
        else:
            samples, total = 0, 0

        samples += 1
        total += children

        self.branches[connections] = (samples, total)

    def getBranchingFactor(self, connections):
        if connections in self.branches:
            samples, total = self.branches[connections]
            return total / samples

        return 0
