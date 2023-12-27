def dyn_fewest_coins(amt, coins):
    """Bottom-up dynamic programming approach"""
    #Generate a list of sub problems to solve
    min_coins = [None] * (amt + 1) 
    # e.g. for amt=10:
    # min_coins: [None, None, None, None, None, None, None, None, None, None, None]
    #   idx/amt:     -     1,    2,    3,    4,    5,    6,    7,    8,    9,   10

    #Iterate over every amount of change up to amt_in_cents
    for cents in range(amt + 1):
        # Worst case: all pennies
        min_coins[cents] = cents 

        # Check with every coin if we can do better
        for c in coins:  
            if c <= cents:
                potential_min = min_coins[cents-c] + 1 # Maybe better? 
                if potential_min < min_coins[cents]:
                    min_coins[cents] = potential_min    

    return min_coins[amt]