from Dijkstra import Node
import sys
from collections import defaultdict
import math


class Graph:
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        if parent[j] == -1:
            print(j, "", end='')
            return
        self.printPath(parent, parent[j])
        print(j, "", end='')

    def printSolution(self, src, des, dist, parent):
        for i in range(1, len(dist)):
            if i == des:
                print("%d --> %d: \nDistance from Source: %d" % (src, i, dist[i]))
                print("Path: ", end='')
                self.printPath(parent, i)

    def dijkstra(self, graph, cor1, cor2):
        global src_node, des_node
        x_src = cor1[0]
        y_src = cor1[1]
        x_des = cor2[0]
        y_des = cor2[1]
        row = len(graph)
        col = len(graph[0])
        matrix = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = graph[i][j].weight
                if i == x_src and j == y_src:
                    src_node = Node.Node(graph[i][j].x, graph[i][j].y, graph[i][j].weight, graph[i][j].name)
                if i == x_des and j == y_des:
                    des_node = Node.Node(graph[i][j].x, graph[i][j].y, graph[i][j].weight, graph[i][j].name)
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src_node.name] = 0
        queue = []
        for i in range(row):
            queue.append(i)

        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if matrix[u][i] and i in queue:
                    if dist[u] + matrix[u][i] < dist[i]:
                        dist[i] = dist[u] + matrix[u][i]
                        parent[i] = u
        self.printSolution(src_node.name, des_node.name, dist, parent)


def main():
    g = Graph()
    graph = [[Node.Node(0, 0, 0, 0), Node.Node(0, 1, 4, 1), Node.Node(0, 2, 0, 2), Node.Node(0, 3, 0, 3),
              Node.Node(0, 4, 0, 4), Node.Node(0, 5, 0, 5), Node.Node(0, 6, 0, 6), Node.Node(0, 7, 8, 7),
              Node.Node(0, 8, 0, 8)],
             [Node.Node(1, 0, 4, 0), Node.Node(1, 1, 0, 1), Node.Node(1, 2, 8, 2), Node.Node(1, 3, 0, 3),
              Node.Node(1, 4, 0, 4), Node.Node(1, 5, 0, 5), Node.Node(1, 6, 0, 6), Node.Node(1, 7, 11, 7),
              Node.Node(1, 8, 0, 8)],
             [Node.Node(2, 0, 0, 0), Node.Node(2, 1, 8, 1), Node.Node(2, 2, 0, 2), Node.Node(2, 3, 7, 3),
              Node.Node(2, 4, 0, 4), Node.Node(2, 5, 4, 5), Node.Node(2, 6, 0, 6), Node.Node(2, 7, 0, 7),
              Node.Node(2, 8, 2, 8)],
             [Node.Node(3, 0, 0, 0), Node.Node(3, 1, 0, 1), Node.Node(3, 2, 7, 2), Node.Node(3, 3, 0, 3),
              Node.Node(3, 4, 9, 4), Node.Node(3, 5, 14, 5), Node.Node(3, 6, 0, 6), Node.Node(3, 7, 0, 7),
              Node.Node(2, 8, 0, 8)],
             [Node.Node(4, 0, 0, 0), Node.Node(4, 1, 0, 1), Node.Node(4, 2, 0, 2), Node.Node(4, 3, 9, 3),
              Node.Node(4, 4, 0, 4), Node.Node(4, 5, 10, 5), Node.Node(4, 6, 0, 6), Node.Node(4, 7, 0, 7),
              Node.Node(3, 8, 0, 8)],
             [Node.Node(5, 0, 0, 0), Node.Node(5, 1, 0, 1), Node.Node(5, 2, 4, 2), Node.Node(5, 3, 14, 3),
              Node.Node(5, 4, 10, 4), Node.Node(5, 5, 0, 5), Node.Node(5, 6, 2, 6), Node.Node(5, 7, 0, 7),
              Node.Node(4, 8, 0, 8)],
             [Node.Node(6, 0, 0, 0), Node.Node(6, 1, 0, 1), Node.Node(6, 2, 0, 2), Node.Node(6, 3, 0, 3),
              Node.Node(6, 4, 0, 4), Node.Node(6, 5, 2, 5), Node.Node(6, 6, 0, 6), Node.Node(6, 7, 1, 7),
              Node.Node(5, 8, 6, 8)],
             [Node.Node(7, 0, 8, 0), Node.Node(7, 1, 11, 1), Node.Node(7, 2, 0, 2), Node.Node(7, 3, 0, 3),
              Node.Node(7, 4, 0, 4), Node.Node(7, 5, 0, 5), Node.Node(7, 6, 1, 6), Node.Node(7, 7, 0, 7),
              Node.Node(6, 8, 7, 8)],
             [Node.Node(8, 0, 0, 0), Node.Node(8, 1, 0, 1), Node.Node(8, 2, 2, 2), Node.Node(8, 3, 0, 3),
              Node.Node(8, 4, 0, 4), Node.Node(8, 5, 0, 5), Node.Node(8, 6, 0, 6), Node.Node(8, 7, 7, 7),
              Node.Node(7, 8, 0, 8)]]
    g.dijkstra(graph, (0, 0), (4, 8))


main()
