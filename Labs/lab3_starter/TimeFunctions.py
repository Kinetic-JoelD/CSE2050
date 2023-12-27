import time

def time_function(func, args, n_trials = 10):
    """ Returns the number of seconds to run func with a argument."""
    
    # Creating the min function with infinity as the default
    min = float('inf')

    #Loops through however many trials the user wants
    for i in range(n_trials):       
        #Grab the time at the beginning, run the function, grab the time at the end
        start = time.time()
        func(args)
        end = time.time()

        # Compute how long it took from start to end and find the minimum time there was going through the trials
        if end - start < min:
            min = end - start
    
    #returns the minimum time out of all the trials
    return min


def time_function_flexible(func, args, n_trials = 10):
    """ Returns the number of seconds to run func with multiple arguments."""

    # Creating the min function with infinity as the default
    min = float('inf')

    #Loops through however many trials the user wants
    for i in range(n_trials):
        #Grab the time at the beginning, run the function, grab the time at the end
        start = time.time()
        func(*args)
        end = time.time()

        # Compute how long it took from start to end and find the minimum time there was going through the trials
        if end - start < min:
            min = end - start
    
    #returns the minimum time out of all the trials
    return min


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000)) 