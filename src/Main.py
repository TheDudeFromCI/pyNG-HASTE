import StandardLibrary
import MathLibrary
import Algorithm
import time


if __name__ == '__main__':
    container = Algorithm.GraphContainer()
    env = Algorithm.Environment()
    tree = Algorithm.SearchTree(container, env)

    container.push(Algorithm.buildGraph([
        StandardLibrary.InputIntegerFunction(),
        StandardLibrary.InputIntegerFunction(),
        StandardLibrary.InputBoolFunction(),
    ], StandardLibrary.OutputIntegerFunction()))

    env.addAxiom(StandardLibrary.MaxConnectionsAxiom(10))

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
    env.addFunction(StandardLibrary.IfFunction(
        StandardLibrary.IntegerDataType()))
    env.addFunction(StandardLibrary.IfFunction(
        StandardLibrary.NumberDataType()))

    env.addFitnessTest(StandardLibrary.FewerConnectionsFitness(magnitude=0.5))

    env.addHeuristic(StandardLibrary.PreferSmallerHeuristic())
    env.addHeuristic(StandardLibrary.RandomHeuristic())

    env.addTest(StandardLibrary.InputOutputTest([2, 7, True], [9]))
    env.addTest(StandardLibrary.InputOutputTest([5, 1, False], [5]))
    env.addTest(StandardLibrary.InputOutputTest([9, 3, False], [27]))
    env.addTest(StandardLibrary.InputOutputTest([6, 6, True], [12]))
    env.addTest(StandardLibrary.AllInputsUsedTest(3))

    print('Running...')
    startTime = time.time()

    iterations = 0
    while not container.isEmpty() and len(container.solutions) == 0:
        tree.nextItr()
        iterations += 1

        if iterations % 50000 == 0:
            print('Iteration: {}, Open: {}, Solutions: {}'.format(
                iterations, len(container.graphs), len(container.solutions)))
            print(container.graphs[-1])

    endTime = time.time()
    elapsedTime = endTime - startTime

    print('Finished in {} iterations. ({:.1f} s)'.format(iterations, elapsedTime))
    print('Solutions:', len(container.solutions))

    limit = 3
    for solution in container.solutions:
        print()
        print(solution)

        limit -= 1
        if limit == 0:
            break
