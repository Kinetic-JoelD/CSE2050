class Entry:
    def __init__(self, item, priority):
        """Creates a new entry with given priority"""
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """Compares priority of two entries"""
        return self.priority == other.priority

    def __lt__(self, other):
        """Compares based on priority of two entries"""
        return self.priority < other.priority

    def __repr__(self):
        """String representation of Entry objects"""
        return f"Entry(item={self.item}, priority={self.priority})"

class Heap:
    def __init__(self):
        """Constructor method for a new Heap object"""
        self._len = 0
        self._L = []

    def __len__(self):
        """Returns number of items in heap"""
        return len(self._L)

    # Static methods do not get access to self or class - they are
    # useful when grouping a method that does not need to modify
    # instance or class variables into a class' namespace
    @staticmethod
    def idx_parent(idx):
        """Returns index of parent in heap, or None if idx is root"""
        left = 0
        right = None

        while left:
            pass



    @staticmethod
    def idx_left(idx):
        """Returns index of left child, or None if idx has no left child"""
        return idx * 2 + 1
        


    @staticmethod
    def idx_right(idx):
        """Returns index of right child, or None if idx has no right child"""
        return idx * 2 + 2


    def insert(self, item, priority):
        """Inserts item with given priority to heap"""
        self._L.append(Entry(item=item, priority=priority))
        self._upheap(len(self._L)-1)

    def _upheap(self, idx):
        """Upheaps item at index until heap is heap-sorted"""
        # Find the pareent index


        #  Swap if unbalanced

        i_p = Heap.idx_parent(idx)

        while i_p is not None and self._L[i_p] < self._L[idx]:
            self._L[i_p], self._L[idx] = self._L[idx], self._L[i_p]
            idx = i_p
            i_p = Heap.idx_parent(i_p)

    def remove_min(self):
        """Removes and returns item with minimum priority"""


    def _idx_min_child(self, idx):
        """Returns index of minimum child if it exists, else None"""
        
    def _downheap(self, idx):
        """Repeatedly downheaps from idx until heap is heap-ordered again"""

    def is_heap_sorted(self, idx=0):
        """Returns True (False) if every branch of heap is heap-sorted"""
        # Note - the method generally doesn't exist. I add it here for educational purposes (makes it a 
        # bit easier to check if your heap code is working when starting out).

        idx_left = Heap.idx_left(idx) if Heap.idx_left(idx) < len(self) else None
        idx_right = Heap.idx_right(idx) if Heap.idx_right(idx) < len(self) else None

        # recursively call on left and right
        if idx_left:
            #  <-------Child is bigger ------->    <---- Reursive call on left --->
            if self._L[idx] > self._L[idx_left] or not self.is_heap_sorted(idx_left): return False

        if idx_right:
            #  <-------Child is bigger ------->    <---- Reursive call on right ---->
            if self._L[idx] > self._L[idx_right] or not self.is_heap_sorted(idx_right): return False

        # everything at subheap rooted here is heap sorted 
        return True