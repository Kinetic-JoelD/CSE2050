def fibonacci(k):
    old, new = 1, 1 # first two fibonacci numbers
    for i in range(1, k):
        old, new = new, old+new

    return new
    
def fibonacci_recr(k):
    #Edge cases
    if k == 0:
        return k

    #Base case
    if k in (0, 1): return 1

    return fibonacci_recr(k - 1) + fibonacci_recr(k-2)

def fibonacci_recr_memoized(k):
    pass

def _fibonacci_recr_memoized(k, solved):
    if k in solved:
        pass
    return _fibonacci_recr_memoized(k, dict{0:1,1:1,})


if __name__ == '__main__':
    # Set up functions + solutions
    fns = [fibonacci, fibonacci_recr, fibonacci_recr_memoized]
    fibonaccis = {0:1, 1:1, 2:2, 3:3, 4:5, 5:8, 6:13, 7:21, 8:34, 9:55, 10:89,}

    # test all functions
    for fn in fns:
        for k in fibonaccis:
            assert fn(k) == fibonaccis[k]
        print(f"{fn.__name__} works!")


    # use known correct fun (fibonacci) to generate answers for new func (fibonacci_recr)
    for i in range(100):
        fib_iter = fibonacci(i)
        fib_recr = fibonacci_recr(i)
        assert fib_iter == fib_recr
    print("recursive works up to 100")

    # # use known correct fun (fibonacci) to generate answers for new func (fibonacci_recr_memoized)
    # for i in range(100):
    #     fib_iter = fibonacci(i)
    #     fib_recr_memo = fibonacci_recr_memoized(i)
    #     assert fib_iter == fib_recr_memo
    # print("memoized recursive works up to 100")