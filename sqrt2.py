class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v):
        self.edges.append((u, v))
        self.vertices.add(u)
        self.vertices.add(v)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1


g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

parent = {}
rank = {}
for v in g.vertices:
    parent[v] = v
    rank[v] = 0

g.union(parent, rank, g.find(parent, 0), g.find(parent, 1))
g.union(parent, rank, g.find(parent, 1), g.find(parent, 2))

print("Edges:", g.edges)
print("Vertices:", g.vertices)
print("Parent:", parent)
print("Rank:", rank)