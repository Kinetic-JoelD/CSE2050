import queue
###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1: Giancarlo Nophal                                            #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################


class Graph:
    def __init__ (self, V, E):
        raise NotImplementedError("This is wrong.")

    def is_connected(self, v1, v2): 
        """ Returns True (False) if there is (is not) a path between v1 and v2 """
        
        if v1 in self.V and v2 in self.V:
            locations = self.bfs(v1).keys()

            if v2 in locations:
                return True
            
        return False
            
    
    def bfs(self, v):
        """ Returns a breadth-first search tree. You must return the tree in a dictionary. """
        # initializions
        visited = {v}
        queue = [v] 
        prev = {v: None}
        
        # While the queue is not empty 
        while queue:
            u = queue.pop(0)  # Removes the first vertext and assigns to u
           
            # explores neighbors of u vertex
            for neighbor in self.nbrs(u):
                if neighbor not in visited:
                    # marks neighbor as visited, adds it to visisted and updates previous dictionary
                    visited.add(neighbor)
                    queue.append(neighbor)
                    prev[neighbor] = u
        
        # Returns the tree 
        return prev

    def count_trees(self):
        """ We will use “trees” to describe isolated structures within an overall graph, or “forest”. 
        Should return a list of trees in a graph as well as the number of distinct trees"""
        # Initializing 
        visited = set()
        forest = []
        tree_count = 0
        
        # Iterates through the verticiess
        for vertex in self:
            if vertex not in visited:
                
                # Increments count for a new tree
                tree_count += 1
                
                # Gets a new tree
                tree = self.bfs(vertex)
                
                # adds the tree to the forest
                forest.append(tree)

                # Adds visited to the update
                visited.update(tree.keys())
    
        # Returns the forest and tree_coutn
        return forest, tree_count

class AdjacencySetGraph(Graph):
    def __init__(self, V = set(), E = set()):
        self.V = set(V)
        self.E = {v: set() for v in self.V}
        for (u, v) in E:
            if u in self.V and v in self.V:
                self.E[u].add(v)
                self.E[v].add(u)

    def __iter__(self):
        """ Returns an iterator over all vertices in the graph """
        return iter(self.V)


    def add_vector(self, v):
        """ Adds a vertex to the graph """
        self.V.add(v)
        self.E[v] = set()


    def add_edge(self, e = tuple()):
        """ Adds edge to graph """
        u, v = e
        if u in self.V and v in self.V:
            self.E[u].add(v)
            self.E[v].add(u)

    def nbrs(self, v):
        """ Returns an iterator over all neighbors v"""
        return self.E[v]

class EdgeSetGraph(Graph):
    def __init__(self, V = set(), E = set()):
        self.V = {v for v in V}
        self.E = {e for e in E}

    def __iter__(self):
        """ Returns an iterator over all vertices in the graph """
        return iter(self.V)


    def add_vector(self, v):
        """ Adds a vertex to the graph """
        self.V.add(v)

    def add_edge(self, e = tuple()):
        """ Adds edge to graph """
        u, w = e
        if u not in self.V or w not in self.V:
            raise ValueError("Vertices must be in graph before adding edge.")
        self.E.add(e)


    def nbrs(self, v):
        """ Returns an iterator over all neighbors v"""
        return {w for (u, w) in self.E if u == v}

if __name__ == "__main__":
    myG = AdjacencySetGraph((1,2,3,4,5),((1,2),(2,3),(4,5),(5,1)))
    myG.add_vector(6)

    print(myG.is_connected(5, 6))