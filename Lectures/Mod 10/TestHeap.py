from heap import Entry, Heap
import unittest, random
random.seed(658) # fix seed so we always fail with the same numbers (makes debugging easier)

class TestEntry(unittest.TestCase):
    def setUp(self):
        """A few entries to test"""
        self.e1 = Entry(item='jake', priority=0)
        self.e2 = Entry(item='rachel', priority=0)
        self.e3 = Entry(item='jake', priority=1)

    def test_eq(self):
        """Tests that equality is defined by priority"""
        self.assertEqual(self.e1, self.e2)
        self.assertNotEqual(self.e1, self.e3)
        self.assertNotEqual(self.e2, self.e3)

    def test_lt(self):
        """Tests that less than only looks at priority"""
        self.assertLess(self.e1, self.e3)
        self.assertGreater(self.e3, self.e1)
        self.assertFalse(self.e1 < self.e2)

    def test_repr(self):
        """Tests string representation"""
        self.assertEqual(repr(self.e1), "Entry(item=jake, priority=0)")
        self.assertEqual(repr(self.e2), "Entry(item=rachel, priority=0)")
        self.assertEqual(repr(self.e3), "Entry(item=jake, priority=1)")

class TestHeap(unittest.TestCase):
    # TODO 1: static methods for finding indices in heap
    def test_idx_par(self):
        """Tests that we get the correct parent for a range of indices"""
        self.assertEqual(Heap.idx_parent(0), None)  # level 0

        self.assertEqual(Heap.idx_parent(1), 0)     # level 1
        self.assertEqual(Heap.idx_parent(2), 0)

        self.assertEqual(Heap.idx_parent(3), 1)     # level 2
        self.assertEqual(Heap.idx_parent(4), 1)
        self.assertEqual(Heap.idx_parent(5), 2)
        self.assertEqual(Heap.idx_parent(6), 2)

        self.assertEqual(Heap.idx_parent(7), 3)     # level 3
        self.assertEqual(Heap.idx_parent(8), 3)
        self.assertEqual(Heap.idx_parent(9), 4)
        self.assertEqual(Heap.idx_parent(10), 4)
        self.assertEqual(Heap.idx_parent(11), 5)
        self.assertEqual(Heap.idx_parent(12), 5)
        self.assertEqual(Heap.idx_parent(13), 6)
        self.assertEqual(Heap.idx_parent(14), 6)

    def test_idx_left(self):
        """Tests that we get the correct left child for a range of indices"""
        self.assertEqual(Heap.idx_left(0), 1)     # level 0

        self.assertEqual(Heap.idx_left(1), 3)     # level 1
        self.assertEqual(Heap.idx_left(2), 5)

        self.assertEqual(Heap.idx_left(3), 7)     # level 2
        self.assertEqual(Heap.idx_left(4), 9)
        self.assertEqual(Heap.idx_left(5), 11)
        self.assertEqual(Heap.idx_left(6), 13)

        self.assertEqual(Heap.idx_left(7), 15)     # level 3
        self.assertEqual(Heap.idx_left(8), 17)
        self.assertEqual(Heap.idx_left(9), 19)
        self.assertEqual(Heap.idx_left(10), 21)
        self.assertEqual(Heap.idx_left(11), 23)
        self.assertEqual(Heap.idx_left(12), 25)
        self.assertEqual(Heap.idx_left(13), 27)
        self.assertEqual(Heap.idx_left(14), 29)

    def test_idx_right(self):
        """Tests that we get the correct right child for a range of indices"""
        self.assertEqual(Heap.idx_right(0), 2)     # level 0

        self.assertEqual(Heap.idx_right(1), 4)     # level 1
        self.assertEqual(Heap.idx_right(2), 6)

        self.assertEqual(Heap.idx_right(3), 8)     # level 2
        self.assertEqual(Heap.idx_right(4), 10)
        self.assertEqual(Heap.idx_right(5), 12)
        self.assertEqual(Heap.idx_right(6), 14)

        self.assertEqual(Heap.idx_right(7), 16)     # level 3
        self.assertEqual(Heap.idx_right(8), 18)
        self.assertEqual(Heap.idx_right(9), 20)
        self.assertEqual(Heap.idx_right(10), 22)
        self.assertEqual(Heap.idx_right(11), 24)
        self.assertEqual(Heap.idx_right(12), 26)
        self.assertEqual(Heap.idx_right(13), 28)
        self.assertEqual(Heap.idx_right(14), 30)

    # TODO 2: Insert
    # def test_insert(self):
    #     """Tests that we can add items and stay heap-ordered"""
    #     h = Heap()
    #     n = 100
    #     for i in range(n):
    #         self.assertEqual(len(h), i)         # before adding

    #         item = random.randint(0, 100)       # generate random entry
    #         priority = item
    #         h.insert(item, priority)

    #         self.assertTrue(h.is_heap_sorted()) # after adding

    # TODO 3: remove_min
    # def test_remove_min(self):
    #     """Tests that we can remove_min in correct order and maintain heap-ordering"""
    #     h = Heap()
    #     n = 100
    #     for i in range(n):
    #         self.assertEqual(len(h), i)         # before adding

    #         item = random.randint(0, 100)       # generate random entry
    #         priority = item
    #         h.insert(item, priority)

    #         self.assertTrue(h.is_heap_sorted()) # after adding


    #     old_entry = Entry(item=None, priority=float('-inf'))
    #     for i in range(n):
    #         self.assertEqual(len(h), n-i)                                       # before removing
    #         new_entry = h.remove_min()                                          # remove

    #         self.assertTrue(h.is_heap_sorted())                                 # CHEATER METHOD - typically we don't test this explicitly
            
    #         self.assertGreaterEqual(new_entry.priority, old_entry.priority)     # compare
    #         old_entry = new_entry                                               # prepare for next loop
            
if __name__ == '__main__':
    unittest.main()