from BSTNode import BSTNode

class BSTMap:
    def __init__(self):
        """Creates a new BSTMap"""

    def __setitem__(self, key, value):
        """adds k:v pair to BSTMap"""
        pass

    def __getitem__(self, key):
        """Returns value associated w/ key"""

    def __contains__(self, key):
        """Returns true if key is in BSTMap, false otherwise"""

    def __repr__(self): 
        """Returns string representation of BSTMap"""

if __name__ == '__main__':
     
    bst1 = BSTMap()
    for i in range(8):
        print(f"i = {i}")
        assert not i in bst1            # test contains (false)
        bst1[i] = str(i)
        assert bst1[i] == str(i)        # tests put/get 
        assert i in bst1                # tests contains (true)

    print(bst1)