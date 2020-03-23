from Algorithm import SearchTree, GraphContainer
from multiprocessing import Process, Queue
import time


def runJob(env, container, q):
    tree = SearchTree(container, env)
    iterations = 0

    startTime = time.time()
    for i in range(10000):
        if container.isEmpty():
            break

        tree.nextItr()
        iterations += 1

    q.put((container, iterations))


def startThread(env, container, q):
    tree = None
    itr = 0
    while len(container.graphs) < 250:
        if tree == None:
            tree = SearchTree(container, env)

        tree.nextItr()
        itr += 1

    miniCon = GraphContainer()
    miniCon.graphs = container.graphs[:250]
    container.graphs = container.graphs[250:]

    Process(target=runJob, args=(env, miniCon, q)).start()
    return itr


def findSolutionParrallel(env, container, threadCount):
    startTime = time.time()
    liveThreads = 0
    itr = 0

    q = Queue()
    for i in range(threadCount):
        if container.isEmpty():
            break

        itr += startThread(env, container, q)
        liveThreads += 1

    foundSolution = False
    while liveThreads > 0 and not foundSolution:
        miniCon, iterations = q.get()
        liveThreads -= 1

        itr += iterations

        for graph in miniCon.graphs:
            container.push(graph)

        for solution in miniCon.solutions:
            container.addSolution(solution)
            foundSolution = True

        if not foundSolution:
            while liveThreads < threadCount:
                if container.isEmpty():
                    break

                itr += startThread(env, container, q)
                liveThreads += 1

        endTime = time.time()
        elapsedTime = endTime - startTime
        print('Iterations: {: >9,}, Open: {: >9,}, Solutions: {: >3,}, Time: {: >7,.1f}s ({: >7,.1f}g/s), Threads: {}'
              .format(itr, len(container.graphs), len(container.solutions), elapsedTime, itr / elapsedTime, liveThreads))

    return itr
