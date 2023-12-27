import unittest, random
from Graph import Graph, AdjacencySetGraph, EdgeSetGraph
###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1: Joel Duah                                                   #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################


class GraphTestFactory:
    def setUp(self, GraphDS):
        self._g1 = GraphDS((1,2,3,4,5),((1,2),(2,3),(3,4),(4,5),(5,1)))
        self._g2 = GraphDS((1,2,3,4,5),((1,2),(2,3),(4,5)))
        self._g3 = GraphDS((1,2,3,4,5),((1,2), (3,4)))
        self._g4 = GraphDS((1,2,3,4,5))

        self.Graph = GraphDS()

    def test__init__(self):
        """Tests that a Graph CAN'T be created using the class Graph """
        # Tests that Graph will raise a not implemented error
        with self.assertRaises(NotImplementedError):
            Graph((1,2,3,4,5), ((1,2),(2,3),(4,5),(5,1)))

        # Tests that its an empty vertex set
        self.assertEqual(self.Graph.V, set())

        # Addding vectors
        self.Graph.add_vector(9)
        self.Graph.add_vector(8)
        self.Graph.add_vector(7)
        self.Graph.add_vector(6)
        exp = {9, 8, 7, 6}

        # We got what we expected with vertexes implemented
        self.assertEqual(self.Graph.V, exp)

        self.Graph.add_edge((9,8))
        self.Graph.add_edge((8,7))
        self.Graph.add_edge((7,6))


        # For adjacency graph
        if type(self._g1.E) is dict:
            self.assertIn(9, self.Graph.E.get(8))
            self.assertIn(7, self.Graph.E.get(6))
            

        # For edge graph    
        elif type(self._g1.E) is set:
            self.assertIn((7,6), self.Graph.E)

        

    def testNbrs(self):
        """Tests depending on the datatype of the edges in the graph; Asserts the correct neighbors of a specfied node"""

        if type(self._g1.E) is dict:
            self.assertTrue({3, 5}, self._g1.nbrs(4))
            
        elif type(self._g1.E) is set:
            self.assertTrue({5}, self._g1.nbrs(4))

            
    def testIsConnected(self):
        """ Tests isConnected which is meant to return True (False) if there is (is not) a path between v1 and v2 """
        # Directly Connected to each other
        self._g1.add_vector(7)
        self.assertFalse(self._g1.is_connected(3, 7))
        self._g1.add_edge((3, 7))
        self.assertTrue(self._g1.is_connected(3, 7))

        # Not directly connected 
        self._g2.add_vector(8)
        self.assertFalse(self._g2.is_connected(8, 3))
        self._g2.add_edge((3, 8))
        self.assertTrue(self._g2.is_connected(2, 8))

        # Things that shouldn't be connected
        self.assertFalse(self._g2.is_connected(4, 8))
        self.assertFalse(self._g2.is_connected(5, 8))


    def testBFS(self):
     
        dist_from_vertex = {1:0, 2:1, 5:1, 3:2, 4:2}
        self._g1.bfs(1)
        for vertex in self._g1:
            self.assertTrue(self._g1.bfs(1), dist_from_vertex[vertex])


    def testCountTrees(self):
        """ Tests the count_tress method which returns a forest and count of trees """
        # Tests if multiple graphs have the correct amoutn of trees in their forests
        self.assertTrue(self._g1.count_trees()[1], 1)
        self.assertTrue(self._g2.count_trees()[1], 2)
        self.assertTrue(self._g3.count_trees()[1], 3)
        self.assertTrue(self._g4.count_trees()[1], 5)

        # Tests the approrpriate number of verticies in each tree
        num_verticies = self._g3.count_trees()[0][0].keys()
        self.assertEqual(len(num_verticies), 2)

        num_verticies = self._g3.count_trees()[0][1].keys()
        self.assertEqual(len(num_verticies), 2)

        num_verticies = self._g1.count_trees()[0][0].keys()
        self.assertEqual(len(num_verticies), 5)

        num_verticies = self._g4.count_trees()[0][0].keys()
        self.assertEqual(len(num_verticies), 1)


    def test__iter__(self):
        """Test that the iter function will return through all values in the Vector"""
        Vectors = list()
        for v in self._g1:
            Vectors.append(v)

        self.assertTrue(Vectors, {1,2,3,4,5})


    def testEmptyGraph(self):
        """Test on an brand new empty graph"""
        empty = AdjacencySetGraph()
        empty.add_vector(1)
        empty.add_vector(2)
        empty.add_edge((1,2))
        self.assertEqual({1,2}, empty.V)
        self.assertEqual({1: {2}, 2:{1}}, empty.E)

 

class TestAdjacencySetGraph(unittest.TestCase, GraphTestFactory):
    def setUp(self):
        return GraphTestFactory.setUp(self, GraphDS = AdjacencySetGraph)

class TestEdgeSetGraph(unittest.TestCase, GraphTestFactory):
    def setUp(self):
        return GraphTestFactory.setUp(self, GraphDS = EdgeSetGraph)


if __name__ == "__main__":   
    unittest.main()

