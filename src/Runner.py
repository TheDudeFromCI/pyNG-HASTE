class Runner:
    def __init__(self, graph):
        self.graph = graph
        self.cache = {}

    def findValues(self, inputs):
        self.cache = {}

        for inputIndex in range(len(inputs)):
            self.cache[(inputIndex + 1, 0)] = inputs[inputIndex]

        self.__calculateValues(self.graph.nodes[0])

        outputs = []
        for i in range(len(self.graph.nodes[0].function.inputs)):
            outputs.append(self.cache[(0, i)])

        del self.cache
        return outputs

    def __calculateValues(self, node):
        if (node.index, 0) in self.cache:
            return

        # if isInstance(node, IfFunction):
        # elif isInstance(node, WhileFunction):
        # elif isInstance(node, ForFunction):
        # else:

        inputs = []
        for inputIndex in range(len(node.function.inputs)):
            conn = self.graph.getConnectionTo(node, inputIndex)
            self.__calculateValues(conn.outputNode)

            inputs.append(self.cache[(conn.outputNode.index, conn.outputPlug)])

        if len(node.function.outputs) == 0:
            outputs = inputs
        else:
            outputs = node.function.run(inputs)

        for i in range(len(outputs)):
            self.cache[(node.index, i)] = outputs[i]
