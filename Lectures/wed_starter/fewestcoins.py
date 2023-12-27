from dynamic_fc import dyn_fewest_coins # Dynamic prog soln used for quick testing

def fewest_coins_greedy(amt, coins):
    """Returns the fewest number of coins required to make amt with the given list coins.
    """
    n_coins =0

    coins.sort(reverseTrue)

    for coin in coins:
        while coin < amt:
            n_coins += 1
            amt -= coin

    return n_coins
    

def fewest_coins_recr(amt, coins):
    """Recurisve solution will explore every possible path"""
    
    # Base case 
    if amt in coins: return 1 

    min_coins = float('inf')

    # Don't
    # min_coins = 9999

    for coin in coins:
        if coin < amt:
            n_branch = 1 + fewest_coins_recr(amt-coin, coins)

            if n_branch < min_coins:
                min_coins = n_branch 


def fewest_coins_memo(amt, coins):
    """Recursive, but uses memoization to avoid redundant solutions"""

if __name__ == '__main__':
    fns = [fewest_coins_greedy, fewest_coins_recr, fewest_coins_memo]
    for amt in [50, 63]:
        print(f"amt = {amt}")
        for coins in [[1, 5, 10, 25], [1, 5, 10, 21, 25]]:
            print(f"\tcoins = {coins}")
            for fn in fns:
                try:
                    assert fn(amt, coins) == dyn_fewest_coins(amt, coins)
                    print(f"\t\t{fn.__name__} works!")

                except AssertionError:
                    print(f"\t\t{fn.__name__} fails.")
