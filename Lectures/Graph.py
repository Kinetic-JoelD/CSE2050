class EdgeSet:
    def __init__(self, V = None, E = None):
        self._V = set()
        self._E = set()
        
        if V is not None: 
            for v in V:  self.add_vertex(V)

        if E is not None:    
            for e in E: self.add_edge(E)

    def add_vertex(self, v):
        self._V.add(v)

    def add_edge(self, e):
        self._E.add(e)

    def is_connected(self, v1, v2): 
        # Base case: we have found a connection
        if v1 == v2: return True

        for nbr in self.nbrs(v1):
            if self.is_connected(nbr, v2): return True
        

    def nbrs(self, v):
        """Iterate over neighbors of vertex v"""
        if v in self._V:
            """
            if v in edge: return other 
            # Using frozenset
            """ 
            for edge in self._E:
                if edge[0] == v: yield edge[1]
                elif edge[1] == v: yield edge[0]


        

if __name__ == '__main__':
    #############################################
    #                                           #
    #                                Portland   #
    #                               / 114 miles #
    #                              /            #
    #               ____________Boston          #
    #     101 miles_/         _/                #
    #            _/          /    85 miles      #
    #           /           |                   #
    #        Hartford------Storrs               #
    #       /           27 mi                   #
    #      / 117 mi                             #
    #     /                                     #
    #   NYC                                     #
    #                                           #
    #   DC                                      #
    #                                           #
    #############################################
    Graph = EdgeSet # Use EdgeSet as our data struture
    V = {'DC', 'NYC', 'Hartford', 'Storrs', 'Boston', 'Portland'}
    E = {('Portland', 'Boston'), ('Boston', 'Portland'), 
         ('Bston', 'Storrs') ('Boston', 'Hartford')
         ('Storrs', 'Boston'), ('Storrs', 'Hartford')
         ('Hartford', 'Storrs')


    }
    g = Graph(V, E)

    # Test some True's from `NYC`
    for city in ['Hartford', 'Storrs', 'Boston', 'Portland']:
        print(f"Testing g.is_connected('NYC', {city})")
        assert g.is_connected('NYC', city)
        print(f"g.is_connected('NYC', {city}) works!\n")

        print(f"Testing g.is_connected({city}, 'NYC')")
        assert g.is_connected(city, 'NYC')
        print(f"g.is_connected({city}, 'NYC') works!\n")
    
    # Test a False from `NYC`
    print(f"Testing not g.is_connected('NYC', 'DC')")
    assert not g.is_connected('NYC', 'DC')
    print(f"not g.is_connected('NYC', 'DC') works!\n")

    print(f"Testing not g.is_connected('NYC', 'DC')")
    assert not g.is_connected('DC', 'NYC')
    print(f"not g.is_connected('NYC', 'DC') works!\n")