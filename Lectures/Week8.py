def is_sorted(L):
    return not any(L[i] > L[i + 1] for i in range(len(L) - 1))

def mergesort(L):
    # 1) Divide into subproblems
    # 2) Solve our subproblems
    # 3) Combine sub-solutioons into main solution
    

    # Base case: list with 1 or fewer items
    if len(L) <= 1: return L

    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    left = mergesort(left)
    right = mergesort(right)

    # Start zipping up sub-problems
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i + j] = left[i]
            i += 1
        else:
            L[i + j] = right[j]
            j += 1

        
    L[i + j:] = left[i:] + right[j:] 
    
    return L

if __name__ == "__main__":
    # Create an unsorted list 
    import random
    L= [random.randint(0,10) for i in range(1000)]
    L.append(-1)


    # Sort it 
    assert(not is_sorted(L))
    mergesort(L)
    assert(is_sorted(L))