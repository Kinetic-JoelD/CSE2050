class BSTMap:
    def __init__(self):
        """ Creates a new BSTMAP"""
        self._root = None
        # TODO: Keep track of a set of node:wt pairs

    def __setitem__(self, key, value):
        self._root = self._root.put(key, value) if self._root else BSTNode(key, value) 

    def __getitem__(self, key):
        if self._root is None: raise RuntimeError(f"{key} not in map")

    def __contains__(self, key):
        """ Returns true fi key is in BSTMpa, false otherwise """
        return key in self._root if self._root else False
    

class BSTNode:
    def __init__(self, key, value, left = None, right = None):
        """ Creates  anew BSTNode"""
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.len = 1

    def __len__(self):
        return self.len
    
    def _update_len(self):
        """ Update len (number of nodes in subtree rooted at sef) """
        # Fidn the amount of of nodes in the left and right tree then adds one to get the length of the tree
        w_left = len(self.left) if self.left else 0
        w_right = len(self.right) if self.right else 0
        self.len = w_left + w_right + 1

    def put(self, key, value):
        """ Adds key:value pair to BST, or updates value if key already in BST"""
        # base case - we've hit the key. It's the same key
        if key == self.key: self.value = value

        # key is smaller - go left
        elif key < self.key:
            self.left = self.left.put(key, value) if self.left else BSTNode(key, value)

        # key is bigger - go right
        else:
            self.right = self.right.put(key, value) if self.right else BSTNode(key, value)

        # Update weights on way up (adds O(1) to O(logn) operations)
        self._update_len()
        new_root = self.rebalance()

        return new_root

    def too_heavy(self, node1, node2):
        """Returns True (False) if node1 has >3x as many nodes as node2"""
        # A little confued are these the weight 
        w1 = len(node1) if node1 else 0
        w2 = len(node2) if node2 else 0

        return w1+1 > 3*(w2+1)

    def rebalance(self):
        """Rebalances tree"""

        # Left leg is too heavy
        if self.too_heavy(self.left, self.right):
            # if weight is on inner leg(self.left.right), we have to shift that first
            if self.too_heavy(self.left.right, self.left.left):
                self.left = self.left.rotate_left() # Shift weight outwards
            return self.rotate_right()

        # Right leg is too light
        elif self.too_heavy(self.right, self.left):
            if self.too_heavy(self.right.left, self.right.right):
                self.right = self.right.rotate_right()
            return self.rotate_left()
        
        # Already balanced
        else: return self

    def rotate_right(self):
        """ rotates ndoe to the right (and down), reutnring new root"""
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self._update_len()
        new_root._update_len()

        return new_root

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        return new_root

    def get(self, key):
        """Returns value associated wiht key."""
        if key == self.key: return self.value
        elif key < self.key:
            if self.left is None: raise RuntimeError(f"key {key} not in BST")
            else: return self.left.get(key)

        else:
            if self.right is None: raise RuntimeError(f"key {key} not in BST")
            else: return self.right.get(key)


    def __contains__(self, key):
        if key == self.key: return True

        elif key < self.key: return key in self.left if self.left is not None else False
        else: return key in self.right if self.right is not None else False