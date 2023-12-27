import unittest
import random
import FindPairs

class TestFindPairs(unittest.TestCase):
    def test_find_pairs_naive(self):
        """thoroughly test find_pairs_naive"""
        lst = [4 ,5 ,6, 7, 8, 3, 6, 7]
        self.assertEqual(FindPairs.find_pairs_naive(lst, 10), {(4,6), (3,7), (7,3)})

        lst = []
        self.assertEqual(FindPairs.find_pairs_naive(lst, 0), set())

        lst = [10, 9, 8, 12, 4, 5,2,56, 10000]
        self.assertEqual(FindPairs.find_pairs_naive(lst, 12), {(10,2), (8,4)})

        # Small num -> largest num test
        lst = [1, 2, 3, 4, 5, 6,7, 8, 9]
        self.assertEqual(FindPairs.find_pairs_naive(lst, 5), {(2,3),(1,4)})

        #Largest num -> small numbers test
        lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(FindPairs.find_pairs_naive(lst, 5), {(4, 1), (3, 2)})

        #Target can't be reached at all
        lst = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(FindPairs.find_pairs_naive(lst, 100), set())

        #Empty list provided
        lst = []
        self.assertEqual(FindPairs.find_pairs_naive(lst, 12), set())
        


    def test_find_pairs_opt(self):
        """thoroughly tests find_pairs_opt"""
        lst = [10, 9, 8, 12, 4, 5,2,56, 10000]
        self.assertEqual(FindPairs.find_pairs_opt(lst, 12), {(10,2), (8,4)})

        # Small num -> largest num test
        lst = [1, 2, 3, 4, 5, 6,7, 8, 9]
        self.assertEqual(FindPairs.find_pairs_opt(lst, 5), {(2,3),(1,4)})

        #Largest num -> small numbers test
        lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(FindPairs.find_pairs_opt(lst, 5), {(4,1),(3,2)})

        #Mountain list test
        lst = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(FindPairs.find_pairs_opt(lst, 5), {(2,3),(1,4)})

        #Target can't be reached at all
        lst = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(FindPairs.find_pairs_opt(lst, 100), set())

        #Empty list provided
        lst = []
        self.assertEqual(FindPairs.find_pairs_opt(lst, 12), set())


    def test_find_pairs_opt_random(self):
        """test find_pairs_opt() with a bunch of random numbers/targets using find_pairs_naive"""
        
        n = 20
        randlist = random.sample(range(0, 30), n)
        self.assertEqual(FindPairs.find_pairs_opt(randlist, 9), FindPairs.find_pairs_opt(randlist, 9))


if __name__ == '__main__':
    unittest.main()
