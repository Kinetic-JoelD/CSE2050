def cypher_naive(msg, shift=0, offset=0):
    """Encrypts a message by shifting letters according to ascii value, reversing the string, then
    offsetting the message.
    Time complexity: O(n^2)
    """
    # Setup - convert str to lowercase and initialize return string
    encrypted_str = ''                         

    # Reverse and Shift (SLOW - strings are immutable, so we keep rewriting the string
    for char in msg:
        encrypted_str = chr(ord(char)+shift) + encrypted_str

    # Offset
    encrypted_str = encrypted_str[offset:] + encrypted_str[0:offset]

    # Return
    return encrypted_str

def cypher_opt(msg, shift=0, offset=0):
    """Encrypts a message by shifting letters according to ascii value, reversing the string, then
    offsetting message.
    Time complexity: O(n)
    """
    # Setup - use a list to store letters
    list(msg)
    encrypted_msg = []

    # Reverse and Shift
    for char in range(len(msg)):
        encrypted_msg.append(chr(ord(msg[char])+shift))
    
    encrypted_msg = encrypted_msg[::-1]


    # Offset
    encrypted_msg = encrypted_msg[offset:] + encrypted_msg[:offset]


    # Prepare to return
    # convert your list to a string using ''.join()
    
    return ''.join(encrypted_msg)


# Code below is just to illustrate running times of the two methods 

def time_fn(fn, *args, n_trials=5):
    """Returns minum time to run fn(*args)"""
    t_min = float('inf')

    for i in range(n_trials):
        start = time.perf_counter()
        fn(*args)
        t_run = time.perf_counter()-start
        if t_run < t_min: t_min = t_run

    return t_min

if __name__ == '__main__':
    # Code that uses time and random
    import time
    import random

    # This is provided to show you the running time difference - you should
    # be able to see quadratic running time for cypher_naive
    import time
    import random

    fns = [cypher_naive, cypher_opt]

    # Print header
    print("="*40)
    print(f"{'n':10}", end='')
    for fn in fns:
        print(f"{fn.__name__:15}", end='')
    print()
    print("-"*40)

    # Print body
    for i in range(1, 11):
            n = int(i*10000)
            print(f"{n:<10}", end='')
            msg = ''.join([chr(random.randint(0, 127)) for i in range(n)])
            for fn in fns:
                print(f"{1000*time_fn(fn, msg, 1, 1):<15.4f}", end='')
            print()

    # Pring footer
    print("-"*40)