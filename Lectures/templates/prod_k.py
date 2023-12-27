def factorial(k):
    pass

def factorial_recr(k):
    pass

if __name__ == '__main__':
    # Set up functions + solutions
    fns = [factorial, factorial_recr]
    factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720,}

    # test all functions
    for fn in fns:
        for k in factorials:
            assert fn(k) == factorials[k]
        print(f"{fn.__name__} works!")
    
    # use known correct fun (factorial) to generate answers for new func (factorial_recr)
    for i in range(100):
        assert factorial_recr(i) == factorial(i)
    print("recursive works up to 100")