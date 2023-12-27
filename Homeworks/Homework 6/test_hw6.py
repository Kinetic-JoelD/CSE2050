import unittest, random
from hw6 import is_sorted, bubble_sort, insertion_sort, selection_sort


class TestSortTable(unittest.TestCase):
    def test_bubble_sort(self):

        # Random Generated list
        L = [random.randint(0, 100) for i in range(100)]

        assert(not is_sorted(L))
        bubble_sort(L)
        assert(is_sorted(L))


        # Sorted Generated list
        L = [item for item in range(100)]
        L_sort = L.copy()
        bubble_sort(L)
        self.assertEqual(L, L_sort )


        # Reverse Generated List 
        L = [item for item in range(100)]
        L.reverse()

        assert(not is_sorted(L))
        bubble_sort(L)
        assert(is_sorted(L))

        # End to Front
        L = [item for item in range(100)]

        # Splciing the list ot get 5% from end to the front
        part = int((len(L) * 95) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        assert(not is_sorted(M))
        bubble_sort(M)
        assert(is_sorted(M))
    

        # Front to End
        L = [item for item in range(100)]

        # Splciing the list ot get 5% from front to the end
        part = int((len(L) * 5) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        assert(not is_sorted(M))
        bubble_sort(M)
        assert(is_sorted(M))

    def test_insetion_sort(self):
        # Random Generated list
        L = [random.randint(0, 100) for i in range(100)]

        assert(not is_sorted(L))
        insertion_sort(L)
        assert(is_sorted(L))


        # Sorted Generated list
        L = [item for item in range(100)]
        L_sort = L.copy()
        insertion_sort(L)
        self.assertEqual(L, L_sort )


        # Reverse Generated List 
        L = [item for item in range(100)]
        L.reverse()

        assert(not is_sorted(L))
        insertion_sort(L)
        assert(is_sorted(L))

        # End to Front
        L = [item for item in range(100)]

        # Splciing the list ot get 5% from end to the front
        part = int((len(L) * 95) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        assert(not is_sorted(M))
        insertion_sort(M)
        assert(is_sorted(M))
    

        # Front to End
        L = [item for item in range(100)]

        # Splciing the list ot get 5% from front to the end
        part = int((len(L) * 5) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        assert(not is_sorted(M))
        insertion_sort(M)
        assert(is_sorted(M))

    def test_selection_sort(self):
        # Random Generated list
        L = [random.randint(0, 100) for i in range(100)]

        assert(not is_sorted(L))
        selection_sort(L)
        assert(is_sorted(L))


        # Sorted Generated list
        L = [item for item in range(100)]
        L_sort = L.copy()
        selection_sort(L)
        self.assertEqual(L, L_sort )


        # Reverse Generated List 
        L = [item for item in range(100)]
        L.reverse()

        assert(not is_sorted(L))
        selection_sort(L)
        assert(is_sorted(L))

        # End to Front
        L = [item for item in range(100)]

        # Splciing the list ot get 5% from end to the front
        part = int((len(L) * 95) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        assert(not is_sorted(M))
        selection_sort(M)
        assert(is_sorted(M))
    

        # Front to End
        L = [item for item in range(100)]

        # Splciing the list ot get 5% from front to the end
        part = int((len(L) * 5) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        assert(not is_sorted(M))
        selection_sort(M)
        assert(is_sorted(M))



if __name__ == "__main__":
    unittest.main()