def binary_search_count(L, element):

    if is_sorted(L) == False:
        return 0
    
    start = binary_search(L, element)

    if start is None:
        return 0
    
    end = start
    count = 0
    
    while L[end] == L[start]:
        end += 1
        count += 1
    
    return count

def binary_search(L, element):
    left, right = 0, len(L)

    while left < right:
        median = (left + right) // 2
        if L[median] < element:
            left = median + 1
        else:
            right = median
        
        if left < len(L) and L[left] == element:
            return left
    return None

def is_sorted(L):
    n = len(L)

    for i in range(n - 1):
        if L[i] > L[i + 1]:
            return False
    return True

if __name__ == "__main__":
    L = [1, 2, 2, 2, 2, 3, 4, 5, 6]
    result = binary_search_count(L, 2)
    print("Count of 2 in the list:", result)
