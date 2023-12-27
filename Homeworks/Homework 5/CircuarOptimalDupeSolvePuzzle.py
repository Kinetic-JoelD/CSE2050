def solve_puzzle(board, idx = 0, visited = None , path = None): # Make sure to add input parameters here
    """Returns a tuple of the optimal path and the number of moves required"""
    goal = len(board) - 1

    # 1) Base case: have you found a valid solution?
    if visited is None:
        visited = set()


    # We are at the end of the list
    if idx == goal:
        return [idx], 0 
    

    # Have we been here before is so stop
    if idx in visited:
        return None, None  # No solution


    # This instance we are on is being added to the list 
    visited.add(idx)

    # Value of the index
    place = board[idx]

    # Moving the player that number of spaces Clockwise or Counter-Clock Wise
    CW = (idx + place) % len(board)
    CCW = (idx - place) % len(board)


    CWSolve, CWMoves = solve_puzzle(board, CW, visited)
    CCWSolve, CCWMoves = solve_puzzle(board, CCW, visited)

    if CWSolve is not None and CCWSolve is not None:
        if CWMoves + 1 <= CCWMoves + 1:
            return [idx] + CWSolve, 1 + CWMoves
        else:
            return [idx] + CCWSolve, 1 + CCWMoves
    elif CWSolve is not None:
        return [idx] + CWSolve, 1 + CWMoves
    elif CCWSolve is not None:
        return [idx] + CCWSolve, 1 + CCWMoves
    else:
        return None, None
    
if __name__ == "__main__":
    lst = [1, 3, 10, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    print(solve_puzzle(lst))





