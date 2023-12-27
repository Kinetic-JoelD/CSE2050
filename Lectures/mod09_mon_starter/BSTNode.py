from math import floor, ceil, log2

class BSTNode:
    def __init__(self, key, value, left=None, right=None):
        """Creates a new BSTNode"""
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.weight = 1

    # Update value or add key:value pair
    def put(self, key, value):
        """Adds key:value pair to BST, or updates value if key already in BST""" 
        if self.key == key:
            self.value = value
        
        elif self.key > key:
            if self.left: self.left.put(key, value)
            else: self.left = BSTNode(key, value)
        
        elif self.key < key:
            if self.right: self.right(key, value)
            else: self.right = BSTNode(key, value)
        

        self.update_weight(self) # update weight to keep track of any new nodes added


    def update_weight(self):
        # If self.left.weight if self.left existis or we'll plug in 0 if it doesn't exisist 
        left_weight = self.left.weight if self.left else 0
        right_weight = self.right.weight if self.right else 0
        self.weight = left_weight + right_weight + 1


    def get(self, key):
        """Returns value associated with key."""
        if self.key == key: return self

        if self.key > key:
            if self.left: return self.left.get(key)
        
        if self.key < key:
            if self.right: return self.right.get(key)

        raise KeyError(f"key {key} is not in tree")


    def __contains__(self, key):
        """Returns True if key is in BST rooted at self"""

    def floor(self, key):
        # We found exactly the key
        if self.key == key: return self
        
        # Going down left sub tree return floor from that sub tree or none
        if self.key > key:
            # case 1: return floor(left)
            # case 2: return None 
            if self.left: return self.left.floor(key)
            return None
        
        # We go right 1. We possibly find a better floor that we are on right now, 
        # 2. If there is no floor to the right of the sub node we return self because we had already found the best solution before
        if self.key < key:
            if self.right: 
                temp_floor = self.right.floor(key)
                if temp_floor: return temp_floor
            else: return self
        

    def update_weight(self):
        """Updates weight of a node"""

    def __repr__(self):
        """Returns a string reprsentation of the BST"""
        L_strings = []
        self._repr(L_strings, level = 0)
       
        # L_strings is a list of lists, e.g.:
        # [['   ---4 ---   '],                          # tree level 0
        #  [' -2 - ', '  ', ' -6 - '],                  # tree level 1
        #  ['1 ', '  ', '3 ', '  ', '5 ', '  ', '7 ']]  # tree level 2


        L_joined = [''.join(level) for level in L_strings]  # join levels into 1 string each
        return '\n'.join(L_joined)                         # join all levels into 1 big string

    def _repr(self, L_strings, level):
        # add a new substring the first time we reach this level
        if level == len(L_strings):
            L_strings.append([])

            # check if we have previous aunts/uncles w/o children
            # manually add an offset on the left if we do.
            if level >= 1:
                offset = 0
                for item in L_strings[-2]:
                    offset+= len(item)
                L_strings[-1].append(' '*offset)
        
        
        # Fill in left tree
        if self.left: wa, wb = self.left._repr(L_strings, level+1)
        else: wa=wb=0

        # write this key, including left-buffer 
        key_width = max(len(str(self.key)), 3) # use at least 3 character long keys, so we get nic looking trees
        L_strings[level].append(' '*wa + '-'*wb + f"{self.key:^{key_width}}") 

        # insert spaces to all levels below, so newly added items have the correct left-offset
        for l in range(level+1, len(L_strings)): L_strings[l].append(' '*key_width)

        # fill in the right tree
        if self.right: wc, wd = self.right._repr(L_strings, level+1)
        else: wc=wd = 0

        # add right-buffer to this key
        L_strings[level][-1] += '-'*wc +' '*wd
        
        # return width of left and right trees
        return wa+wb+floor(key_width/2), wc+wd+ceil(key_width/2) 
            

if __name__ == '__main__':

    ### Some basic trees ###
    #    5
    #   4
    #  3
    # 2
    #1
    root = BSTNode(5, '5')
    for i in [4, 3, 2, 1]:
        root.put(i, str(i))
    print(root)
    print()


    # 9
    #  8
    #   7
    #    6
    #     5
    #      4
    #       3
    #        2
    #         1
    root = BSTNode(1, '1')
    for i in range(2, 10):
        root.put(i, str(i))
    print(root)
    print()


    #     4
    #  2       6
    # 1 3   5     7
    #          6.5
    root = BSTNode(4, '4')
    for i in [2, 6, 1, 3, 5, 7, 6.5]:
        assert not i in root
        root.put(i, str(i))
        assert i in root
    print(root)
    print()

    
    #     4
    #  2       6
    # 1 3   5     7
    #          6.5
    root = BSTNode('e', '4')
    for i in 'abcdfg':
        assert not i in root
        root.put(i, str(i))
        assert i in root
    print(root)
    print()
    ### Random tree ###
    import random
    newint = random.randint(0, 1000)
    #print(f"adding {newint}")
    root = BSTNode(newint, str(newint))
    for i in range(30):
        newint = random.randint(0, 1000)
        #print(f"adding {newint}")
        root.put(newint, str(newint))

    #import pdb; pdb.set_trace()
    print(root)
