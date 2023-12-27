import itertools
class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, leftVal):
        """ Add right value """
        self.left = leftVal

    def add_right(self, rightVal):
        """ Adds right value"""
        self.right = rightVal

    def evaluate(self):
        """
         Evaluates the subtree rooted at the node. 
        """

        if self.value in BETNode.CARD_VAL_DICT:
            # if the current node is a card value, return the value and sets 0 to float inf
            return BETNode.CARD_VAL_DICT[self.value]
        if self.value == '0':
            return float('inf')

        # Node is an operator so go through the children
        elif self.value in BETNode.OPERATORS:
            left_value = self.left.evaluate()
            right_value = self.right.evaluate()

            # Evaluating for all the operations
            if self.value == '+':
                return left_value + right_value
            elif self.value == '-':
                return left_value - right_value
            elif self.value == '*':
                return left_value * right_value
            elif self.value == '/':
                # handling division by 0
                if right_value == 0 or right_value == float('inf'):
                    return float('inf')
                # regular division
                return left_value / right_value
        
        # An error occurred so we raise a runtime error     
        else:
            raise RuntimeError("There is an error somewhere")
        
    
    def __repr__(self):
        """Return a string representation of the binary expression tree rooted at this node."""
        # Check if the current node's value is an operator
        if self.value in self.OPERATORS:
            #formatting it to be casio style'
            return f'({self.left}{self.value}{self.right})'
        else:
            # returns value if its not an operator
            return str(self.value)

        
def create_trees(cards):
    """Return a set of every valid tree for a given collection of 4 cards"""
    all_trees = set()
    valids = set()

    # Generate all permutations of operators
    operators_permutations = list(itertools.product(BETNode.OPERATORS, repeat = 3))

    # Goes through all permutations of cards and operators together and checks if its a valid tree adding it to all_trees
    for card_permutation in list(itertools.permutations(cards)):
        for operators_permutation in operators_permutations:
            combined = list(operators_permutation) + list(card_permutation)

            # All possible permutation of operators and cards (~7.7 million)
            myUniverse = itertools.permutations(combined)

            # Checks each permutation to see if it satisfies a tree and then adds it to all_tree
            for universe in myUniverse:
                # CCXCCXX
                if universe[0] in BETNode.CARD_VAL_DICT and universe[1] in BETNode.CARD_VAL_DICT and universe[2] in BETNode.OPERATORS and universe[3] in BETNode.CARD_VAL_DICT and universe[4] in BETNode.CARD_VAL_DICT and universe[5] in BETNode.OPERATORS and universe[6] in BETNode.OPERATORS:
                    valids.add(universe)

                # CCXCXCX
                elif universe[0] in BETNode.CARD_VAL_DICT and universe[1] in BETNode.CARD_VAL_DICT and universe[2] in BETNode.OPERATORS and universe[3] in BETNode.CARD_VAL_DICT and universe[4] in BETNode.OPERATORS and universe[5] in BETNode.CARD_VAL_DICT and universe[6] in BETNode.OPERATORS:
                    valids.add(universe)

                # CCCXXCX
                elif universe[0] in BETNode.CARD_VAL_DICT and universe[1] in BETNode.CARD_VAL_DICT and universe[2] in BETNode.CARD_VAL_DICT and universe[3] in BETNode.OPERATORS and universe[4] in BETNode.OPERATORS and universe[5] in BETNode.CARD_VAL_DICT and universe[6] in BETNode.OPERATORS:
                    valids.add(universe)
                # CCCXCXX
                elif universe[0] in BETNode.CARD_VAL_DICT and universe[1] in BETNode.CARD_VAL_DICT and universe[2] in BETNode.CARD_VAL_DICT and universe[3] in BETNode.OPERATORS and universe[4] in BETNode.CARD_VAL_DICT and universe[5] in BETNode.OPERATORS and universe[6] in BETNode.OPERATORS:
                    valids.add(universe)
                
                # CCCCXXX
                elif universe[0] in BETNode.CARD_VAL_DICT and universe[1] in BETNode.CARD_VAL_DICT and universe[2] in BETNode.CARD_VAL_DICT and universe[3] in BETNode.CARD_VAL_DICT and universe[4] in BETNode.OPERATORS and universe[5] in BETNode.OPERATORS and universe[6] in BETNode.OPERATORS:
                    valids.add(universe)
        

    # Creatng the tree nodes
    for hand in valids:
     # Empty stack to store nodes
        stack = []

        for card in hand:
            # Check if the current card is a card value
            if card in BETNode.CARD_VAL_DICT:
                # Create a new BETNode object with the card value and add it to the stack
                stack.append(BETNode(card))
            # Check if the current card is an operator
            if card in BETNode.OPERATORS:
                # Create a new BETNode object with the operator
                opNode = BETNode(card)
                opNode.add_right(stack.pop())
                opNode.add_left(stack.pop())

                # Add the operator node back to the stack
                stack.append(opNode)

        # Add the root node of the created tree to the set of all trees
        all_trees.add(stack[0])

    return all_trees


def find_solutions(cards):
    """Find all ways to get 24 from the valid trees for a given 4-card universe."""
    # Calling create_trees to get all valid tree
    myTrees = create_trees(cards)
    solutions = set()

    # Iterating through card hands we see if any of the operations add up to 24
    for tree in myTrees:
        if tree.evaluate() == 24:
            solutions.add(tree)
    
    return solutions

