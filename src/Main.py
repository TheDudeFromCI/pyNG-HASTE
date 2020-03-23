import StandardLibrary
import MathLibrary
import Algorithm
from BranchingFactor import BranchingFactor
import time
import math
import Multithreading

if __name__ == '__main__':
    container = Algorithm.GraphContainer()
    env = Algorithm.Environment()
    tree = Algorithm.SearchTree(container, env)

    container.push(Algorithm.buildGraph([
        StandardLibrary.InputNumberFunction(),
        StandardLibrary.InputNumberFunction(),
        StandardLibrary.InputBoolFunction(),
    ], StandardLibrary.OutputNumberFunction()))

    env.addAxiom(StandardLibrary.MaxConnectionsAxiom(50))
    env.addFunction(MathLibrary.AddFunction())
    env.addFunction(MathLibrary.MultiplyFunction())
    env.addFunction(MathLibrary.DivideFunction())
    env.addFunction(MathLibrary.SubtractFunction())
    env.addFunction(MathLibrary.ExponentFunction())
    env.addFunction(StandardLibrary.IfFunction(
        StandardLibrary.NumberDataType()))

    env.addFitnessTest(StandardLibrary.FewerConnectionsFitness(magnitude=0.5))

    env.addTest(StandardLibrary.InputOutputTest([2, 7, True], [9]))
    env.addTest(StandardLibrary.InputOutputTest([5, 1, False], [5]))
    env.addTest(StandardLibrary.InputOutputTest([9, 3, False], [27]))
    env.addTest(StandardLibrary.InputOutputTest([6, 6, True], [12]))
    env.addTest(StandardLibrary.AllInputsUsedTest(3))

    print('Running...')
    Multithreading.findSolutionParrallel(env, container, 8)

    print("Top 3 solutions:")

    limit = 3
    for solution in container.solutions:
        print()
        print(solution)

        limit -= 1
        if limit == 0:
            break
