def find_pairs_naive(lst, target):
    """ A naive function that finds all pairs of integers in the input list that add up to the target integer.
    Time complexity: O(n^2)
    """
    pairs = set()                           # 1
    for i in range(len(lst)):               # n
        for j in range(i+1, len(lst)):      #   n
            if lst[i] + lst[j] == target:   #     2 (add, then compare)
                pairs.add((lst[i], lst[j])) #     1
    return pairs                            # 1
                                            #-------------------------
                                            # 1 + n * (n *(2+1)) + 1 = 3n^2 + 2 = O(n^2)
                                            # Hint - searching a list is expensive! Use a data structure
                                            # with a O(1) search cost instead

def find_pairs_opt(lst, target):
    """Uses a set for O(1) membership testing
    Time complexity: O(n)"""
    
    #Creating the set that will hold the targets
    pairs = set()

    lstcop = lst.copy()
    lstcop = set(lstcop)


    #Iterate through the list
    for num in lst:
        
        # The othr value that may reach the sum
        complement = target - num

        if complement in lstcop:
            # The pair hasn't been made before
            if (complement, num) not in pairs:
                if complement != num:
                    pairs.add((num, complement))             

    return pairs


if __name__ == '__main__':

    mylst = [4 ,5 ,6, 7, 8, 3, 6, 7]
    print(find_pairs_opt(mylst, 10))
        
