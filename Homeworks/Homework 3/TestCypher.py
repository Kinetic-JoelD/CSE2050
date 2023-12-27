import Cypher
import unittest


class TestCypher(unittest.TestCase):

    def test_cypher_naive(self):
        """should shift letters + message appropriately"""
        msg = "Hi, my name is Ash"
        expected_out = "B!tj!fnbo!zn!-jIit"
        self.assertEqual(Cypher.cypher_naive(msg, shift=1, offset=2), expected_out)

    # TODO
    def test_opt_provided(self):
        """should shift letters + message appropriately"""
        msg = "Hi, my name is Ash"
        expected_out = "B!tj!fnbo!zn!-jIit"
        print(Cypher.cypher_opt(msg, shift=1, offset=2))
        self.assertEqual(Cypher.cypher_opt(msg, shift=1, offset=2), expected_out)

    # TODO
    def test_opt_random(self):
        """Tests our optimized algorithm using the naive version"""
        msg = 'Apple Pie is better than Pumpkin Pie!'
        self.assertEqual(Cypher.cypher_opt(msg, shift = 1, offset = 2), Cypher.cypher_naive(msg, shift = 1, offset = 2))
        



if __name__ == '__main__':
    unittest.main()