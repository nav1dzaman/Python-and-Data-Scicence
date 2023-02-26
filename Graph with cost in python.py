# importing networkx
import networkx as nx
import numpy as np
# importing matplotlib.pyplot
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, nodes, directed=True):
        self.nodes = nodes
        self.graph_list = {}
        self.graph_list_cost = {}
        self.directed = directed

        for all_node in self.nodes:
            self.graph_list[all_node] = []

    def add_edge(self, x, y, cost):
        if self.directed:
            self.graph_list[x].append(y)
            self.graph_list_cost[(x, y)] = cost
        else:
            self.graph_list[x].append(y)
            self.graph_list[y].append(x)

    def degree(self, node):
        deg = len(self.graph_list[node])
        return deg

    def print_graph(self):
        for node in self.graph_list:
            print(node, "->", self.graph_list[node])


nde = int(input("enter the number of nodes"))

NODES = []

for i in range(0, nde):
    x = input()
    NODES.append(x)

grph = Graph(NODES)

edge = 3

for i in range(edge):
    x = input()
    y = input()
    cst = int(input())
    grph.add_edge(x, y, cst)

grph.print_graph()
