def sum_k(k):
    total = 0
    for i in range(k):
        total += (i+1)
    return total

def sum_k_const(k):
    return (k/2)*(k+1)

def sum_k_recr(k):
    # Edge case
    if k == 0: return 0 
    elif k == 1: return 1

    # Base case
    if k in (1, 0 ):return k
    return k + sum_k_recr(k-1)

if __name__ == '__main__':
    # Set up functions + solutions
    fns = [sum_k, sum_k_const, sum_k_recr]
    sums = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15, 6:21, 7:28, 8:36, 9:45, 10:55}

    # test all functions
    for fn in fns:
        for k in sums:
            assert fn(k) == sums[k]
        print(f"{fn.__name__} works!")

    # use known correct fun (sum_k_const) to generate answers for new func (sum_k_recr)
    for i in range(100):
        assert sum_k_recr(i) == sum_k_const(i)
    print("recursive works up to 100")