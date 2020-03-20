import StandardLibrary
import MathLibrary
import Algorithm
from BranchingFactor import BranchingFactor
import time
import math


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
    env.addHeuristic(StandardLibrary.PreferSmallerHeuristic(magnitude=-0.1))

    env.addTest(StandardLibrary.InputOutputTest([2, 7, True], [9]))
    env.addTest(StandardLibrary.InputOutputTest([5, 1, False], [5]))
    env.addTest(StandardLibrary.InputOutputTest([9, 3, False], [27]))
    env.addTest(StandardLibrary.InputOutputTest([6, 6, True], [12]))
    env.addTest(StandardLibrary.AllInputsUsedTest(3))

    print('Running...')
    startTime = time.time()

    branching = BranchingFactor()

    iterations = 0
    while not container.isEmpty():
        target = container.peek()

        openCount = len(container.graphs)
        connections = len(target.connections)
        tree.nextItr()

        newCount = len(container.graphs)
        branching.addSample(connections, newCount - openCount + 1)

        iterations += 1

        if iterations % 10000 == 0 or container.isEmpty():
            endTime = time.time()
            elapsedTime = endTime - startTime

            print('Iteration: {:,}, Open: {}, Solutions: {}, Time: {:.1f}s'.format(
                iterations, len(container.graphs), len(container.solutions), elapsedTime))
            print(target)

            print("Branching factor")
            scale = 1
            last = 0
            for i in range(10):
                bf = branching.getBranchingFactor(i)
                last = scale
                scale *= bf
                print('  {}) {: >4.2f} => {:,}'.format(
                    i, bf, math.floor(scale + last)))

    print("Top 3 solutions:")

    limit = 3
    for solution in container.solutions:
        print()
        print(solution)

        limit -= 1
        if limit == 0:
            break
