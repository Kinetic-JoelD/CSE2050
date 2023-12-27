from BSTNode import BSTNode

# Public interface: users only interact with the class BSTMap.
# Methods in BSTSet often call BSTNode methods, which do the heavy lifting.
class BSTSet:
    def __init__(self):
        self._head = None

    # classic iteration (bad)
    def __iter__(self):
        return iter(self._head)

    # generator based iteration (good)
    def in_order(self):
        yield from self._head.in_order()



    # TODO: How should these methods call the BSTNode methods?
    def put(self, key):
        if self._head is None:
            # if the set is empty, create a new head node with the specified key
            self._head = BSTNode(key)
        else:
            # otherwise, call the put method on the head node to add the key to the tree
            self._head.put(key)

    def pre_order(self):
        # define a generator for pre-order traversal of the set
        if self._head is not None:
            yield from self._head.pre_order()

    def post_order(self):
        # define a generator for post-order traversal of the set
        if self._head is not None:
            yield from self._head.post_order()