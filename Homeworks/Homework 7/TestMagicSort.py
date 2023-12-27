import unittest, random
from MagicSort import linear_scan, reverse_list, insertion_sort, quick_sort, merge_sort,  magic_sort


class Test_linear_scan(unittest.TestCase):
   def test_linear_scan(self):
    """
    Testing linear scan a function that does a single linear scan of a list L 
    and returns an integer denoting which case that lists fits into (return value will be one of {0, 1, 2, 3})
    """
    ns = [7,10, 100, 1000]

    # Generating reverse ordered list of varying lengths
    for i in range(len(ns)):

        L = [item for item in range(ns[i])]
        L.reverse()
        self.assertEqual(linear_scan(L), 3)

    # Generating sorted lists of varying lengths
    for i in range(len(ns)):
        L = [item for item in range(ns[i])]
        self.assertEqual(linear_scan(L), 1 or 2)


    # Regular list not sorted items with duplicates
    L = [random.randint(0, 100) for i in range(30)]
    self.assertEqual(linear_scan(L), 0)


    #Edge case empty list
    L = []
    self.assertEqual(linear_scan(L), 0)


class Test_reverse_list(unittest.TestCase): 
   def test_reverse_list(self):
        """
        Function that reverses a list efficientyly
        """
        
        # Regular reverse list
        mylst =  [1,2,3,4]
        mylstExp =  [4,3,2,1]
        reverse_list(mylst)
        self.assertEqual(mylst, mylstExp)


        # Odd length list
        mylst =  [1, 2, 3, 4, 5, 6, 7]
        mylstExp =  [7, 6, 5, 4, 3, 2, 1]
        reverse_list(mylst)
        self.assertEqual(mylst, mylstExp)

        # Even length list
        mylst =  [1, 2, 3, 4, 5, 6, 7, 8]
        mylstExp =  [8 ,7 ,6 ,5 ,4 ,3 ,2 ,1]
        reverse_list(mylst)
        self.assertEqual(mylst, mylstExp)


        # Empty List
        mylst =  []
        mylstExp =  []
        reverse_list(mylst)
        self.assertEqual(mylst, mylstExp)

        # Duplicates
        mylst =  [1, 2, 2, 3, 3, 3]
        mylstExp =  [3, 3, 3, 2, 2, 1]
        reverse_list(mylst)
        self.assertEqual(mylst, mylstExp)

class Test_insertionsort(unittest.TestCase):
   def test_insertion_sort(self):
    """
    Testing a version of insertion sort that only sorts the sublist L[left:right] so we will go up to 
    but not including right if you call this function
    """
      
    # Regular unosrted list
    mylst =  [2, 3, 1, 4]
    mylstExp =  [1, 2,3, 4]
    insertion_sort(mylst)
    self.assertEqual(mylst, mylstExp)

    # Reverse Sorted List 
    mylst = [5,4,3,2,1]
    mylstExp = [1,2,3,4,5]
    insertion_sort(mylst)
    self.assertEqual(mylst, mylstExp)


    # Certain section gets sorted
    mylst = [4, 3, 1, 6, 5, 2]
    mylstExp = [4, 1, 3, 6, 5, 2]
    insertion_sort(mylst, left=1, right=4)
    self.assertEqual(mylst, mylstExp)

    # Empty List
    mylst = []
    insertion_sort(mylst)
    self.assertEqual(mylst, [])
    

class Test_mergesort(unittest.TestCase):
   def test_merge_sort(self):
    # Regular unosrted list
    mylst =  [2, 3, 1, 4]
    mylstExp =  [1, 2,3, 4]
    merge_sort(mylst)
    self.assertEqual(mylst, mylstExp)

    # Reverse Sorted List 
    mylst = [5,4,3,2,1]
    mylstExp = [1,2,3,4,5]
    merge_sort(mylst)
    self.assertEqual(mylst, mylstExp)


    # Certain section gets sorted
    mylst = [4, 3, 1, 6, 5, 2]
    mylstExp = [4, 1, 3, 6, 5, 2]
    merge_sort(mylst, left=1, right=4)
    self.assertEqual(mylst, mylstExp)

    # Empty List
    mylst = []
    merge_sort(mylst)
    self.assertEqual(mylst, [])

class Test_quicksort(unittest.TestCase):
   def test_quick_sort(self):
    # Regular unosrted list
    mylst =  [2, 3, 1, 4]
    mylstExp =  [1, 2,3, 4]
    quick_sort(mylst)
    self.assertEqual(mylst, mylstExp)

    # Reverse Sorted List 
    mylst = [5,4,3,2,1]
    mylstExp = [1,2,3,4,5]
    quick_sort(mylst)
    self.assertEqual(mylst, mylstExp)


    # Certain section gets sorted
    mylst = [4, 3, 1, 6, 5, 2]
    mylstExp = [4, 1, 3, 6, 5, 2]
    quick_sort(mylst, left=1, right=4)
    self.assertEqual(mylst, mylstExp)

    # Empty List
    mylst = []
    quick_sort(mylst)
    self.assertEqual(mylst, [])

    mylst = [-5, -3, -1, -2, -4]
    quick_sort(mylst)
    mylstExp = [-5, -4, -3, -2, -1]
    self.assertEqual(mylst, mylstExp)

class Test_magicsort(unittest.TestCase): 
   def test_magic_sort(self):
    # Regular unosrted list
    mylst =  [2, 3, 1, 4]
    mylstExp =  [1, 2,3, 4]
    magic_sort(mylst)
    self.assertEqual(mylst, mylstExp)

    # Reverse Sorted List 
    mylst = [5,4,3,2,1]
    mylstExp = [1,2,3,4,5]
    magic_sort(mylst)
    self.assertEqual(mylst, mylstExp)

    # Empty List
    mylst = []
    magic_sort(mylst)
    self.assertEqual(mylst, [])

    mylst = [-5, -3, -1, -2, -4]
    magic_sort(mylst)
    mylstExp = [-5, -4, -3, -2, -1]
    self.assertEqual(mylst, mylstExp)
   pass

unittest.main()