import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        """ Tests repr which returns a string representation of the binary expression tree rooted at this node. """

        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """

        # Creating the Binary Expression Tree
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self): 
        """ Tests the evaluate method (Evaluates the subtree rooted at the node) of the BETNode with 1/5 valid trees """
        r"""String representation
            CCXCCXX

               +
              / \
             *   -
            / \ / \
           A  23   4
           
        """
        root = BETNode("+")
        root.add_left(BETNode("*"))
        root.add_right(BETNode("-"))

        root.left.add_left(BETNode("A"))
        root.left.add_right(BETNode("2"))

        root.right.add_left(BETNode("3"))
        root.right.add_right(BETNode("4"))

        expected_eval = 1
        self.assertEqual(root.evaluate(), expected_eval)


    def test_evaluate_tree2(self):
        """ Tests the evaluate method (Evaluates the subtree rooted at the node) of the BETNode with 1/5 valid trees """
        r"""String representation
            CCXCXCX

               +
              / \
             -   4
            / \
           *   3
          / \
         A   2

           
        """
        
        root = BETNode("+")
        root.add_left(BETNode("-"))
        root.add_right(BETNode("4"))

        root.left.add_left(BETNode("*"))
        root.left.add_right(BETNode("3"))

        root.left.left.add_left(BETNode("A"))
        root.left.left.add_right(BETNode("2"))

        expected_eval = 3
        self.assertEqual(root.evaluate(), expected_eval)

    def test_evaluate_tree3(self):
        """ Tests the evaluate method (Evaluates the subtree rooted at the node) of the BETNode with 1/5 valid trees """
        r"""String representation
            CCCXXCX

               +
              / \
             *   4
            / \
           A   -
              / \ 
             2   3

        """
        
        root = BETNode("+")
        root.add_left(BETNode("*"))
        root.add_right(BETNode("4"))

        root.left.add_left(BETNode("A"))
        root.left.add_right(BETNode("-"))

        root.left.right.add_left(BETNode("2"))
        root.left.right.add_right(BETNode("3"))

        expected_eval = 3
        self.assertEqual(root.evaluate(), expected_eval)

    def test_evaluate_tree4(self):
        """ Tests the evaluate method (Evaluates the subtree rooted at the node) of the BETNode with 1/5 valid trees """
        r"""String representation
            CCCXCXX

               *
              / \
             A   +
                / \
               -   4
              / \
             2   3

        """
        
        root = BETNode("*")
        root.add_left(BETNode("A"))
        root.add_right(BETNode("+"))

        root.right.add_left(BETNode("-"))
        root.right.add_right(BETNode("4"))

        root.right.left.add_left(BETNode("2"))
        root.right.left.add_right(BETNode("3"))

        expected_eval = 3
        self.assertEqual(root.evaluate(), expected_eval)

    def test_evaluate_tree5(self):
        """ Tests the evaluate method (Evaluates the subtree rooted at the node) of the BETNode with 1/5 valid trees """
        r"""String representation
            CCCCXXX

               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4


        """
        
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))

        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))

        expected_eval = -5
        self.assertEqual(root.evaluate(), expected_eval)


class TestCreateTrees(unittest.TestCase):
    def test_hand1(self): 
        cards = 'AKJQ'
        expected_value = 7680

        self.assertEqual(len(create_trees(cards)), expected_value)

        cards = 'AKJA'
        expected_value = 3840

        self.assertEqual(len(create_trees(cards)), expected_value)
        
    def test_hand2(self): 
        cards = '5694'
        expected_value = 7680

        self.assertEqual(len(create_trees(cards)), expected_value)

        cards = '5695'
        expected_value = 3840

        self.assertEqual(len(create_trees(cards)), expected_value)
        

class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        cards = '1111'
        expected_output = 0

        self.assertEqual(len(find_solutions(cards)), expected_output)

    def test_A23Q(self):
        cards = 'A23Q'
        expected_output = 33
        self.assertEqual(len(find_solutions(cards)), expected_output)
        
unittest.main()