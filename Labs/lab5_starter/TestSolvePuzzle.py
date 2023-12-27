from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                myBoard = [3, 6, 4, 1, 3, 4, 2, 0]
                self.assertEqual(puzzle(myBoard), True)

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                b1 = [3, 0, 2, 1]
                self.assertTrue(puzzle(b1))

                b2 = [2, 0, 1, 2]
                self.assertTrue(puzzle(b2))

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                b1 = [3, 1, 2, 3, 0]
                idx = 2
                expected_output = True
                result = puzzle(b1, idx)
                self.assertEqual(result, expected_output)

                board = [2, 5, 1, 3, 0, 4]
                self.assertTrue(puzzle(board))
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                myBoard = [3, 4, 1, 2, 0] 
                self.assertEqual(puzzle(myBoard), False)

                board = [2, 3, 0, 1]
                self.assertFalse(puzzle(board))

                board = [0, 1, 2, 3, 4]
                self.assertFalse(puzzle(board))

unittest.main()