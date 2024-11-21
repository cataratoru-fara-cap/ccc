import numpy as np

class Graph:
    def __init__(self, numNodes):
        self.N = numNodes
        self.G = np.full((numNodes, numNodes), False)
        self.nodeInfo = {}
        self.edgeInfo = {}

    def setNodeInfo(self, i, info):
        self.nodeInfo[i] = info

    def getNodeInfo(self, i):
        return self.nodeInfo[i]

    def addEdge(self, i, j):
        self.G.add_edge(i, j)

    def removeEdge(self, i, j):
        self.G.remove_edge(i, j)

    def setEdgeInfo(self, i, j, info):
        self.edgeInfo[(i, j)] = info

    def getEdgeInfo(self, i, j):
        return self.edgeInfo[(i, j)]

    def dfs(self, x):
        print(x)
        visited = set()
        visited.add(x)

        for y in self.G.neighbors(x):
            if y not in visited:
                self.dfs(y)

    def bfs(self, S):
           if y not in visited:
                    visited.add(y)
                    queue.append(y)

    def biparti(self, S):
        queue = []
        visited = set()

        queue.append(S)
        visited.add(S)

        while queue:
            x = queue.pop(0)
            for y in self.G.neighbors(x):
                if y not in visited:
                    visited.add(y)
                    queue.append(y)

# Create the graph
g = Graph(8)

# Add edges
g.addEdge(0, 4)
g.addEdge(2, 4)
g.addEdge(6, 4)
g.addEdge(7, 4)
g.addEdge(7, 5)
g.addEdge(6, 5)
g.addEdge(3, 7)
g.addEdge(1, 3)

print("DFS starting from node 4:")
g.dfs(4)

print("BFS starting from node 4:")
g.bfs(4)        
visited = set()

queue.append(S)
visited.add(S)

while queue:
    x = queue.pop(0)
    print(x)
    for y in self.G.neighbors(x):
        if y not in visited:
            visited.add(y)
            queue.append(y)

    def biparti(self, S):
        queue = []
        visited = set()

        queue.append(S)
        visited.add(S)

        while queue:
            x = queue.pop(0)
            for y in self.G.neighbors(x):
                if y not in visited:
                    visited.add(y)
                    queue.append(y)

# Create the graph
g = Graph(8)

# Add edges
g.addEdge(0, 4)
g.addEdge(2, 4)
g.addEdge(6, 4)
g.addEdge(7, 4)
g.addEdge(7, 5)
g.addEdge(6, 5)
g.addEdge(3, 7)
g.addEdge(1, 3)

print("DFS starting from node 4:")
g.dfs(4)

print("BFS starting from node 4:")
g.bfs(4)
