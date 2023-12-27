import unittest
from turnTracker import TurnTracker

# Implement your unit tests here

class TestTurnTracker(unittest.TestCase):
    def setUp(self):
        self.game1 = TurnTracker()  

    def testAddPlayer(self):
        """ 
        Tests the addPlayer method which adds a player to the turn tracker after the last player that was added to the tracker
        """
        
        # Empty List
        self.assertEqual(self.game1.numberOfPlayers(), 0)

        self.game1.addPlayer('Jack')
        self.game1.addPlayer('Jill')
        self.game1.addPlayer('Fill')
        self.game1.addPlayer('Dawn')


        # Normal Case
        self.assertEqual(self.game1.numberOfPlayers(), 4)

    def testNextPlayer(self):
        """
        Testing the testNextPlayer which returns the next player in the turn order based on the current game state
        """

        self.game1.addPlayer('Jack')
        self.game1.addPlayer('Jill')
        self.game1.addPlayer('Fill')
        self.game1.addPlayer('Dawn')

        # Tests that it moves through the game normally
        self.assertEqual(self.game1.nextPlayer(), 'Jack')
        self.assertEqual(self.game1.nextPlayer(), 'Jill')
        self.assertEqual(self.game1.nextPlayer(), 'Fill')
        self.assertEqual(self.game1.nextPlayer(), 'Dawn')
        self.assertEqual(self.game1.nextPlayer(), 'Jack')

        


    def testNumberofPlayers(self):
        """
        Tests the testNumberofPlayers method which returns the number of players in the turn tracker
        """

        self.game1.addPlayer('Jack')
        self.game1.addPlayer('Jill')
        self.game1.addPlayer('Fill')
        self.game1.addPlayer('Dawn')
        self.game1.addPlayer('Trevor')
        self.game1.addPlayer('Joel')
        self.game1.addPlayer('Rocky')
        self.game1.addPlayer('Bowie')

        # Normal case for length
        self.assertEqual(self.game1.numberOfPlayers(), 8)

    def testSkipNextPlayer(self):
        """
        Tests the skipNextPlayer method which causes the next player in the turn order to be skipped
        """

        self.game1.addPlayer('Jack')
        self.game1.addPlayer('Jill')
        self.game1.addPlayer('Fill')
        self.game1.addPlayer('Dawn')

        self.game1.skipNextPlayer()

        # Skipping at the head 
        self.assertEqual(self.game1.nextPlayer(), 'Jill')

        # Moving through the list normally
        self.game1.nextPlayer()
        self.game1.nextPlayer()


        # Back to the beginning
        self.assertEqual(self.game1.nextPlayer(), 'Jack') # Seeing if Jack appears again

        # Skipping every other one
        self.game1.skipNextPlayer()
        self.game1.nextPlayer()
        self.game1.skipNextPlayer()
        self.assertEqual(self.game1.nextPlayer(), 'Jack') # Doing it a bunch



    def testReverseTurnOrder(self):
        """
        Tests the reverseTurnOrder method whihc reverses the current direction of the turn order
        """

        self.game1.addPlayer('Jack')
        self.game1.addPlayer('Jill')
        self.game1.addPlayer('Fill')
        self.game1.addPlayer('Dawn')

        # Playing normal game
        self.game1.nextPlayer()
        self.game1.nextPlayer()
        self.game1.nextPlayer()
        self.game1.skipNextPlayer() 
        self.game1.nextPlayer()
        self.game1.reverseTurnOrder() 
        self.game1.nextPlayer()
        
        # Normal case
        self.assertEqual(self.game1.nextPlayer(), 'Fill')

        #reverseOrder with only one player
        game2 = TurnTracker()

        game2.addPlayer('Joel')
        game2.reverseTurnOrder()
        game2.nextPlayer()
        self.assertEqual(game2.nextPlayer(), 'Joel')

        game3 = TurnTracker()

        # No players in the game 
        game3.reverseTurnOrder()
        self.assertEqual(game3.nextPlayer(), None)


if __name__ == '__main__':
    unittest.main()
    