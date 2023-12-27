class Entry:
    def __init__(self, item, priority):
        # Inidializing stuff
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        # = function
        return self.priority == other.priority
    
    def __lt__(self, other):
        # less than fucntion
        return self.priority < other.priority

    def __repr__(self):
        # string representation
        return f"Entry(item = {self.item}, priority = {self.priority})"

class MinHeap:
    def __init__(self):
        self._len = 0
        self._L  = []

    def __len__(self):
        """Retruns the length of the list"""
        return len(self._L)

    @staticmethod
    def idx_parent(idx):
        """Finds the parent of whatever item is at that index"""
        return (idx - 1)//2 if idx else None

    @staticmethod
    def idx_left(idx):
        """Find the index of the left child"""
        return idx * 2 + 1

    @staticmethod
    def idx_right(idx):
        """Finds the index of the right child"""
        return idx * 2 + 2

    def insert(self, item, priority):
        """Inserts a new item into the heap"""
        # Add the entry to the list
        self._L.append(Entry(item, priority))

        # To keep the heap it has to reorganize
        # self._upheap(len(self._L)-1)

    def _upheap(self, idx):
        i_p = MinHeap.idx_parent(idx)
        # While i_p is within scope of the item at at idx is less than its parent 
        while i_p is not None and self._L[idx] < self._L[i_p]:
            # Swaps the child and parent around
            self._L[idx], self._L[i_p] = self._L[i_p], self._L[idx]

            # the index is changed to the parent
            idx = i_p
            # looks at the parent of the new index to
            i_p = MinHeap.idx_parent(idx)

            # Starts all over again

    def remove_min(self):
        min_entry = self._L[0]

        self._L[0] = self._L[-1] # Basically replacing the first item (min) with the last itme so removing it too

        self._L.pop() # Removing that duplicate of the last item

        self._downheap(0) # Downheap starting from the first eleemtn

        return min_entry 

    def _idx_min_child(self, idx):
        """ Returns index of minimum child if it exists """
        i_left = MinHeap.idx_left(idx)
        i_right = MinHeap.idx_right(idx)

        if i_left >= len(self): return None  # If the i_left goes beyond the bounds of the list
        if i_right >= len(self): return i_left # If the i_right goes beyond the bounds of the list

        return i_left if self._L[i_left] < self._L[i_right] else i_right  # 
    

    def _downheap(self,idx):
        i_min = self._idx_min_child(idx)

        while i_min is not None and self.L[i_min] < self._L[idx]:
            self._L[i_min], self._L[idx] = self._L[idx], self._L[i_min]
            idx = i_min
            i_min = self._idx_min_child(idx)


    def is_heap(self, idx=0):
        """ Returns True (False) if every item is no greater than it children """
        idx_right = self.idx_right(idx) # Getting right child idx
        idx_left = self.idx_left(idx) # Getting left child idx

        if idx_left > len(self._L)-1: 
            idx_left = None # If the i_left goes beyond the bounds of the list

        if idx_right > len(self._L)-1:  # If the i_right goes beyond the bounds of the list
            idx_right = None


        if idx_right is not None: # This is a complete Tree with a left and right child
            left = self.is_heap(idx_left)
            if left is False:
                return False
            
            right = self.is_heap(idx_right)
            if right is False: 
                return False

            
            elif self._L[idx_right] < self._L[idx] or self._L[idx_left] < self._L[idx]: # If the left or right child is less than the parent returns false
                return False
            else:
                return True
            
        
        elif idx_left is not None: # There is only a left child
            left = self.is_heap(idx_left)
            if left == False:
                return False
            
            elif self._L[idx_left] < self._L[idx]:
                return False
        
        return True
        

            
        


if __name__ == "__main__":
    myTree = MinHeap()

    myTree.insert('Billy5', 1)
    myTree.insert('Billy1', 2)
    myTree.insert('Billy1', 3)
    myTree.insert('Billy1', 4)
    myTree.insert('Billy1', 5)
    myTree.insert('Billy1', 6)
    myTree.insert('Billy1', 7)
    myTree.insert('Billy1', 8)
    myTree.insert('Billy1', 9)
    myTree.insert('Billy1', 10)





    print(myTree._L)
    print(myTree.is_heap(0))


