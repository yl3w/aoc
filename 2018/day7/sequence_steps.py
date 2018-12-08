# --- Day 7: The Sum of Its Parts ---
# https://adventofcode.com/2018/day/7

import re
from collections import defaultdict
from itertools import chain

def readSpecification(filename):
    """read the input and return a 2-tuple (A,C) representing a dependency/edge"""
    edges = []
    with open(filename) as f:
        pattern = re.compile(r"Step (.*) must be finished before step (.*) can begin.")
        for line in f:
            match =  pattern.match(line)
            edges.append((match.group(1), match.group(2)))

    return edges

def makeGraph(edges):
    """generates a adjancency list representation of a graph"""
    graph = {}
    nodes = set()
    for edge in edges:
        source, destination = edge
        nodes.add(source)
        nodes.add(destination)
        adjacentEdges = graph.get(source, [])
        adjacentEdges.append(destination)
        graph[source] = adjacentEdges

    for node in nodes:
        if node not in graph:
            graph[node] = []

    return graph

def computeInDegree(graph):
    """computes count of edges into a each vertex of the graph"""
    indegree = {}
    for vertex in graph.keys():
        indegree[vertex] = 0
    
    for destination in chain.from_iterable(graph.values()):
        indegree[destination] += 1
    
    return indegree

def findCandidateSteps(graph):
    """returns list of vertices with no incoming edges"""
    indegree = computeInDegree(graph)
    return list(map(lambda t: t[0], filter(lambda t: t[1] == 0, indegree.items())))

def walk(graph):
    """walks/topological sorts the graph with additional ordering on vertices"""
    order = ''
    while len(graph) > 0:
        s = sorted(findCandidateSteps(graph))[0]
        order += s
        del graph[s]

    return order

def invertGraph(edges):
    """created a predecessor graph as an adjacency list"""
    predecessors = defaultdict(set)
    for edge in edges:
        source, destination = edge
        predecessors[destination].add(source)

    return predecessors

def findLatestEnd(vertices, endTimes):
    """find the latest end time for listed vertices"""
    if len(vertices) == 0:
        return 0

    return max(map(lambda p : endTimes[p], vertices))

def performWork(graph, predecessors, workers=2, baseTime=0):
    workerTimeline = [0]*workers
    endTimes = {}

    while(len(graph)) > 0:
        steps = findCandidateSteps(graph)
        for s in steps:
            endForPredecessors = findLatestEnd(predecessors[s], endTimes)
            startForWorker = min(workerTimeline)
            startTime = max(endForPredecessors, startForWorker)
            worker = workerTimeline.index(startForWorker)
            duration = baseTime + ord(s) - ord('A') + 1
            endTime = startTime + duration
            endTimes[s] = endTime
            workerTimeline[worker] = endTime
            del graph[s]

    return max(workerTimeline)


#edges = readSpecification('sample.input')
edges = readSpecification('production.input')
print('Solution to part 1 ' + walk(makeGraph(edges)))
print('Solution to part 2 ' + str(performWork(makeGraph(edges), invertGraph(edges), 5, 60)))
