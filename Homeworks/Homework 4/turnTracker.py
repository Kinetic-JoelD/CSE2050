###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################



class TurnTrackerNode:
# Hint: This class should look just like the LinkNode class (the doubly linked list version)
    def __init__(self, player, prev = None, next = None):
        self._player = player
        self._prev = prev
        self._next = next

        if prev is not None:
            self._prev._next = self
        if next is not None:
            self._next._prev = self

    def __repr__(self):
        """String representation of the node"""
        return f"Uno Player:({self._player})"





class TurnTracker:
# Hint: This class shares a lot of functionality/logic with the DoublyLinkedList class from the textbook.
# A good place to start is by looking at that DoublyLinkedList class and examining which methods are going
# to be similar to those needed by the TurnTracker. Then start adjusting those methods to suit your needs here.
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

        self._nextPlayer = self._head
        self._reversed = False
        self._skipping = False


    def addPlayer(self, player):
        """ 
        Adds a player to the turn tracker after the last player that was added to the tracker
        """

        # Creating a node that is the new player
        newPlayer = TurnTrackerNode(player)

        # Initializign an empty list pointing at itself
        if self._head is None:

            self._head = self._tail = newPlayer
            self._head._next = self._tail
            self._tail._prev = self._head
        else:
            # Making sure the newPlayer pointers are pointing the correct way for a circular DLL
            newPlayer._prev = self._tail
            newPlayer._next = self._head

            # Updating the tail next and head previous pointers to be the newPlayer
            self._tail._next = newPlayer
            self._head._prev = newPlayer

            # Finally updating the tail to be the newPlayer method
            self._tail = newPlayer

        #Updating the length of the list
        self._len += 1
        

    def nextPlayer(self):
        """
        Returns the next player in the turn order based on the current game state
        """

        # Is this an empty list?
        if self._head is None:
            raise RuntimeError
        
        # Has the player method not been initialized before?
        if self._nextPlayer is None:

            # Has the skip card been played the first turn? 
            if self._skipping == True:
                self._nextPlayer = self._head._next
        
                # grab the player from nextPlayer, resetting the skip, and returning the player whos turn it is
                whosTurn = self._nextPlayer._player
                self._skipping = False
                return whosTurn

            # The head is assigned as the next player
            else:
                self._nextPlayer = self._head

                whosTurn = self._nextPlayer._player
                self._skipping = False
                return whosTurn

        # The current players turn
        whosTurn = self._nextPlayer._player

        # The skip card has been played
        if self._skipping == True:
            
            # Has the reverse card been played as well?
            if self._reversed == True:
                self._nextPlayer = self._nextPlayer._prev._prev
                
                whosTurn = self._nextPlayer._player
                self._skipping = False
                return whosTurn

            if self._reversed == False:
                self._nextPlayer = self._nextPlayer._next._next
                
                whosTurn = self._nextPlayer._player
                self._skipping = False
                return whosTurn

        else:
            # Has the reverse card been played?
            if self._reversed == False:
                self._nextPlayer = self._nextPlayer._next
                
                whosTurn = self._nextPlayer._player
                return whosTurn

            if self._reversed == True:
                self._nextPlayer = self._nextPlayer._prev
                
                whosTurn = self._nextPlayer._player
                return whosTurn
        
        


    def numberOfPlayers(self):
        """
        Returns the number of players in the turn tracker
        """
        # Updated when other methods that affect the length run (addPlayer)
        return self._len

    def skipNextPlayer(self):
        """
        Causes the next player in the turn order to be skipped
        """

        # Switching the state of the skip function
        self._skipping = True

    def reverseTurnOrder(self):
        """
        Reverses the current direction of the turn order
        """

        # Switching states each time the function is called
        if self._reversed is False:
            self._reversed = True
        else:
            self._reversed = False
