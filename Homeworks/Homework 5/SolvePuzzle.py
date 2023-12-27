def solve_puzzle(board, idx=0, path=None, moves=0): # Make sure to add input parameters here
    """Returns a tuple of the optimal path and the number of moves required"""
    goal = len(board) - 1

    # 1) Make an empty list to keep track of the path
    if path is None:
        path = []

    # We are at the end of the list
    if idx == goal:
        path.append(idx)
        return path, moves

    # Check if the index is out of bounds or if we've visited it before
    if idx < 0 or idx > goal or idx in path:
        return None, None  # No solution

    # Add the current index to the path
    path.append(idx)

    # Value of the index
    place = board[idx]



    # Moving the player that number of spaces Clockwise or Counter-Clockwise
    CW = idx + place  # Calculate the index after moving clockwise
    CCW = idx - place  # Calculate the index after moving counterclockwise

    # Recursive calls with updated path and moves count
    CWSolve, CWMoves = solve_puzzle(board, CW, path[:], moves + 1)
    CCWSolve, CCWMoves = solve_puzzle(board, CCW, path[:], moves + 1)




    # Choose the better solution between clockwise and counterclockwise
    if CWSolve is not None and CCWSolve is not None:
        if CWMoves <= CCWMoves:
            return CWSolve, CWMoves
        else:
            return CCWSolve, CCWMoves
    elif CWSolve is not None:
        return CWSolve, CWMoves
    elif CCWSolve is not None:
        return CCWSolve, CCWMoves
    else:
        return None, None
    
if __name__ == "__main__":
    lst = [8, 8, 4, 2, 1, 9, 7, 4, 4, 6]
    print(solve_puzzle(lst))





