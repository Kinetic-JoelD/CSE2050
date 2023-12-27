def solve_puzzle(board, idx = 0, visited = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    goal = len(board) - 1
    distance = goal - idx

    # 1) Base case: have you found a valid solution?
    if visited is None:
        visited = set()

    # We are at the end of the list
    if idx == goal:
        return True
    
    # Have we been here before is so stop
    elif idx in visited:
        return False
    

    # This instance we are on is being added to the list 
    visited.add(idx)

    # Value of the index
    place = board[idx]

    # Moving the player that number of spaces Clockwise or Counter-Clock Wise
    CW = (idx + place) % len(board)
    CCW = (idx - place) % len(board)

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    CWSolve = solve_puzzle(board, CW, visited)
    CCWSolve = solve_puzzle(board, CCW, visited)
    
    
    return CWSolve or CCWSolve

