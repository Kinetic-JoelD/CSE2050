class Graph:
    def __init__(self, V, E):
        """ Creates an ege set graph """
        self.V = V
        self.E = E

    def add_vertex(self, v):
        """ adds vertex to graph """
        self.V.add(v)

    def add_edge(self, e):
        """ adds edge to graph """
        self.E.add(e)

    def nbrs(self,v):
        """ Returns an iterator over all neighbors of vertex v """
        for edge in self.E:
            if v == edge[0]: yield edge[1]
            if v == edge[1]: yield edge[0]

    def dfs(self, v, visited = None):
        """ """
        # TODO: implement dfs that always adds neighbors to stack in alphabetical order
        if visited is None:
            visited = set()

        visited.add(v)
        print(v)

        neighbors = sorted(self.nbrs(v))
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
            


if __name__ == "__main__":
    myGraph = Graph({1,2,3,4},{(1,2)})
    myGraph.add_vertex(6)

    myGraph.dfs(2)
