import StandardLibrary
import MathLibrary
import Algorithm


if __name__ == '__main__':
    container = Algorithm.GraphContainer()
    container.push(Algorithm.buildGraph([
        MathLibrary.InputIntegerFunction(),
        MathLibrary.InputIntegerFunction(),
        MathLibrary.InputIntegerFunction(),
    ], MathLibrary.OutputIntegerFunction()))

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
    env.addTest(StandardLibrary.InputOutputTest([1, 5, 2], [12]))
    env.addTest(StandardLibrary.AllInputsUsedTest(3))

    tree = Algorithm.SearchTree(container, env)

    print('Running...')
    iterations = 0
    while not container.isEmpty():
        tree.nextItr()
        iterations += 1

    print('Finished in', iterations, 'iterations.')
    print('Solutions:', len(container.solutions))

    for solution in container.solutions:
        print()
        print(solution)
