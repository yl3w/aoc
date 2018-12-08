# --- Day 7: The Sum of Its Parts ---
# https://adventofcode.com/2018/day/7

import re
import itertools
from pprint import pprint
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
    indegree = {}
    for vertex in graph.keys():
        indegree[vertex] = 0
    
    for destination in chain.from_iterable(graph.values()):
        indegree[destination] += 1
    
    return indegree

def findCandidateSteps(graph):
    indegree = computeInDegree(graph)
    return list(map(lambda t: t[0], filter(lambda t: t[1] == 0, indegree.items())))

def sort(graph):
    order = ''
    while len(graph) > 0:
        s = sorted(findCandidateSteps(graph))[0]
        order += s
        del graph[s]

    return order


#edges = readSpecification('sample.input')
edges = readSpecification('production.input')
graph = makeGraph(edges)
#pprint(graph)
print(sort(graph))
