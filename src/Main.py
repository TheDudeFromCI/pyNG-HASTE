import StandardLibrary
import MathLibrary
import Algorithm

if __name__ == '__main__':
    graph = Algorithm.NodeGraph()
    graph.addNode(MathLibrary.OutputNumberFunction())
    graph.addNode(MathLibrary.InputNumberFunction())
    graph.addNode(MathLibrary.InputNumberFunction())

    container = Algorithm.GraphContainer()
    container.push(graph)

    env = Algorithm.Environment()
    env.addAxiom(StandardLibrary.MaxConnectionsAxiom(5))
    env.addFunction(MathLibrary.AddFunction())
    env.addFunction(MathLibrary.MultiplyFunction())
    env.addFunction(MathLibrary.DivideFunction())
    env.addFunction(MathLibrary.SubtractFunction())
    env.addFunction(MathLibrary.ExponentFunction())
    env.addFunction(MathLibrary.AddIntFunction())
    env.addFunction(MathLibrary.MultiplyIntFunction())
    env.addFunction(MathLibrary.DivideIntFunction())
    env.addFunction(MathLibrary.SubtractIntFunction())
    env.addFunction(MathLibrary.ExponentIntFunction())
    env.addFitnessTest(StandardLibrary.FewerConnectionsFitness(magnitude=0.5))

    tree = Algorithm.SearchTree(container, env)

    print('Running...')
    iterations = 0
    while not container.isEmpty():
        tree.nextItr()
        iterations += 1

    print('Finished in', iterations, 'iterations.')
    print('Solutions:', len(container.solutions))

    if len(container.solutions) > 0:
        print('\nSolution 0:')
        print(container.solutions[0])
