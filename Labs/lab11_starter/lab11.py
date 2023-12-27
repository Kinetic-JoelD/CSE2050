class Graph_ES:
    """Graph class using an edge set to store edges."""
    def __init__(self, Vs=set(), Es=set()):
        self._vertices = {v for v in Vs}
        self._edges = {e for e in Es}

    def add_vertex(self, v):
        self._vertices.add(v)

    def remove_vertex(self, v):
        self._vertices.discard(v)
        self._edges = {(u, w) for u, w in self._edges if u != v and w != v}

    def add_edge(self, e):
        u, w = e
        if u not in self._vertices or w not in self._vertices:
            raise ValueError("Vertices must be in graph before adding edge.")
        self._edges.add(e)

    def remove_edge(self, e):
        self._edges.discard(e)

    def _neighbors(self, v):
        return {w for (u, w) in self._edges if u == v}

    def __len__(self):
        return len(self._vertices)

    def __iter__(self):
        return iter(self._vertices)

class Graph_AS:
    def __init__(self, Vs, Es):
        self.V = set(Vs)
        self.E = {v: set() for v in self.V}
        for (u, v) in Es:
            if u in self.V and v in self.V:
                self.E[u].add(v)
                self.E[v].add(u)

    def add_vertex(self, v):
        self.V.add(v)
        self.E[v] = set()

    def remove_vertex(self, v):
        self.V.discard(v)
        for u in self.E[v]:
            self.E[u].remove(v)
        del self.E[v]

    def add_edge(self, e):
        u, v = e
        if u in self.V and v in self.V:
            self.E[u].add(v)
            self.E[v].add(u)

    def remove_edge(self, e):
        u, v = e
        self.E[u].discard(v)
        self.E[v].discard(u)

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)

    def _neighbors(self, v):
        return self.E[v]