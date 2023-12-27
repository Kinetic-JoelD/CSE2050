###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1: Giancarlo Nophal                                            #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

import random
import timeit


# TODO: Implement bubble_sort function.
# Ensure it is adaptive
def bubble_sort(L):
    """
    Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    """
    # Counter for how many swaps occurred
    swaps = 0
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(L) - 1):
            # Compares left and right 
            if L[i] > L[i + 1]:
                swaps += 1

                # Swap occurrs if the left is larger than the right 
                L[i], L[i + 1] = L[i + 1], L[i]
                unsorted = True
    
    return swaps

# TODO: Implement insertion_sort function.
# Ensure it is adaptive
def insertion_sort(L):
    """
    Builds the final sorted list one item at a time. Takes each element from the input list and 
    inserts it into its correct position within the sorted part of the list.
    """
    # Counter for how many swaps occurred
    swaps = 0
    n = len(L)
    for i in range(n): 
        j=n-i-1
        while j < n - 1 and L[j]>L[j+1]:
            swaps += 1
            L[j], L[j+1] = L[j+1], L[j]
            j+=1
    return swaps

# TODO: Implement selection_sort function.
# Ensure it is adaptive
def selection_sort(L):
    """
    Works by dividing the input list into two parts: the sorted part and the unsorted part.
    finds the minimum element from the unsorted part and moves it to the beginning of the sorted part.
    """

    # Counter for how many swaps occurred
    swaps = 0
    n = len(L)

    # Find the next biggest item
    for i in range(n-1):
        max_index=0
        for index in range(n - i):
            if L[index] > L[max_index]:
                max_index = index
        swaps += 1

        # Swap that item to the correct spot
        L[n-i-1], L[max_index] = L[max_index], L[n-i-1]

    return swaps

def bubble_sort_time(L):
    """
    Find the amount of time it takes for bubble sort to run
    """
    startTime = timeit.default_timer()
    swaps = bubble_sort(L)
    myTime = f'{(timeit.default_timer() - startTime):.5f}'
    return swaps, myTime

def insertion_sort_time(L):
    """
    Find the amount of time it takes for insertion sort to run
    """
    startTime = timeit.default_timer()
    swaps = insertion_sort(L)
    myTime = f'{(timeit.default_timer() - startTime):.5f}'
    return swaps, myTime

def selection_sort_time(L):
    """
    Find the amount of time it takes for selection sort to run
    """
    startTime = timeit.default_timer()
    swaps = selection_sort(L)
    myTime = f'{(timeit.default_timer() - startTime):.5f}'
    return swaps, myTime

def printMyTable():
    # Printing Header
    width = 120
    Scenarios = ['Random', 'Sorted', 'Reverse', 'Move front to end', 'Move end to front']
    ns =  [2000, 3000, 4000, 5000]
    print(f"{'Scenario' : ^20}|{'List Size' : ^20}|{'Bubble Sort' : ^20}|{'Insertion Sort' : ^20}|{'Selection Sort' :^20}") 
    print('-'*width)
    print(f"{'' : ^20}|{'' : ^20}|{'Swap, time' : ^20}|{'Swap, time' : ^20}|{'Swap, time' :^20}") 
    print('-'*width)


    # Case A: Random list generated
    for i in range(len(ns)):

        # Generating a random list
        L = [random.randint(0, 100) for i in range(ns[i])]
        L_bubble = L.copy()
        L_insertion = L.copy()
        L_selection = L.copy()

        # Printing results into table
        print(f"{'Random' : ^20}|{ns[i] : ^20}|{f'{bubble_sort_time(L_bubble)}' : ^20}|{f'{insertion_sort_time(L_insertion)}' : ^20}|{f'{selection_sort_time(L_selection)}' : ^20}")


    print('-'*width)

    # Case B: Sorted list
    for i in range(len(ns)):

        # Generating sorted list
        L = [item for item in range(ns[i])]
        L_bubble = L.copy()
        L_insertion = L.copy()
        L_selection = L.copy()

        print(f"{'Sorted' : ^20}|{ns[i] : ^20}|{f'{bubble_sort_time(L_bubble)}' : ^20}|{f'{insertion_sort_time(L_insertion)}' : ^20}|{f'{selection_sort_time(L_selection)}' : ^20}")

    print('-'*width)


    # Case C: Reverse Order List
    for i in range(len(ns)):

        #Generating reverse ordered list
        L = [item for item in range(ns[i])]
        L.reverse()

        L_bubble = L.copy()
        L_insertion = L.copy()
        L_selection = L.copy()

        print(f"{'Reverse' : ^20}|{ns[i] : ^20}|{f'{bubble_sort_time(L_bubble)}' : ^20}|{f'{insertion_sort_time(L_insertion)}' : ^20}|{f'{selection_sort_time(L_selection)}' : ^20}")

    print('-'*width)


    # Case D:  Move 5% of the elements in a sorted list from end to front
    for i in range(len(ns)):
        L = [item for item in range(ns[i])]

        # Splciing the list ot get 5% from end to the front
        part = int((len(L) * 95) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        M_bubble = M.copy()    
        M_insertion = M.copy()  
        M_selection = M.copy()    
    

        print(f"{'Move End to Front' : ^20}|{ns[i] : ^20}|{f'{bubble_sort_time(M_bubble)}' : ^20}|{f'{insertion_sort_time(M_insertion)}' : ^20}|{f'{selection_sort_time(M_selection)}' : ^20}")

    print('-'*width)


    # Case E: Move 5% of the elements in a sorted list from front to end
    for i in range(len(ns)):
        L = [item for item in range(ns[i])]

        # Splciing the list ot get 5% from front to the end
        part = int((len(L) * 5) / 100)
        startSplice = L[:part]
        endSplice = L[part:]
        M = endSplice + startSplice

        M_bubble = M.copy()    
        M_insertion = M.copy()  
        M_selection = M.copy()    
    

        print(f"{'Move Front to End' : ^20}|{ns[i] : ^20}|{f'{bubble_sort_time(M_bubble)}' : ^20}|{f'{insertion_sort_time(M_insertion)}' : ^20}|{f'{selection_sort_time(M_selection)}' : ^20}")




#Feel free to write any additional functions that may be necessary 
# to populate the results required in part 2.
def is_sorted(L):
    """
    Checks to see if a list is sortd
    """
    for i in range(len(L) -1):
        if L[i] > L[i + 1]: return False
    return True

# Testing the sorting algorithms do their thing
if __name__ == "__main__":
    L = [random.randint(0,10) for i in range(1000)]
    L.append(-1)


    assert(not is_sorted(L))
    selection_sort(L)
    assert(is_sorted(L))


'''
Part 3: Conclusion

Based on your performance analysis, write a conclusion that addresses the following points:

1. Provide a ranking of the sorting algorithms based on their performance in each scenario. Which sorting algorithm performed best in each case (Random, Sorted, Reverse Order, Move End to Front, Move Front to End), and why do you think it performed better?

2. Explain how the number of swaps made by each algorithm affects both efficiency and time complexity across different scenarios.

3. Discuss the impact of the initial order of data on how well each algorithm performs. Explain why some algorithms perform differently on sorted, reversed, or random lists.
'''

"""
1. 
Random: #1. Selection Sort #2. Insertion Sort #3. Bubble Sort
Sorted: #1. Bubble Sort #2. Insertion Sort #3. Selection Sort
Reverse: #1. Selection Sort #2. Insertion Sort #3. Bubble Sort
Move End to Front: #1. Bubble Sort #2. Selection Sort #3. Insertion Sort
Move Front to End: #1. Insertion Sort #2. Selection Sort #3. Bubble Sort

2. 

The number of swaps made by each algorithm has a direct effect on efficiency and time 
complexity because swapping is rearranging elements in a list. With selection sort it has a 
consistently the same number of swaps because it checks against each element in a list at least 
once except for the first element and this gives it a consistent running time of O(n^2). While 
insertion sort and bubble sort are adaptive and can have varying time complexities based on the 
list. 

3. 

For sorted data Bubble sort and insertion sort work well because the number of swaps they
have to do are none while selection goes through the entire list. 

For random data selection sort works the best because it is consistent with the number of swaps 
it has to do while insertion and bubble sort are up in the air

For move end to front bubble sort works the best because it's moving the max values to the end 
of  the list while insertion sort has to move through the sorted list a bunch of times to sort it, and 
selection sort is consistent again with its swaps and its time.

For move front to end insertion sort works the best because it doesn’t have to move as much 
stuff around in the sorted list it has while bubble sort struggles with sorting small stuff at the end 
of a list. 

"""


'''
Include the results table here
Example:
 Scenario     |List Size |    Bubble Sort     |   Insertion Sort   |     Selection      
------------------------------------------------------------------------------------------ 
                 |          |    Swaps, time     |    Swaps, time     |    Swaps, time     
------------------------------------------------------------------------------------------ 
     Random      |   2000   | (1001534, 0.27795) | (1001534, 0.15458) |  (1994, 0.06522)   
     Random      |   3000   |                    |                    |    
     Random      |   4000   |                    |                    |    
     Random      |   5000   |                    |                    |    
------------------------------------------------------------------------------------------
     Sorted      |   2000   |                    |                    |    
     Sorted      |   3000   |                    |                    |       
     Sorted      |   4000   |                    |                    |       
     Sorted      |   5000   |                    |                    |       
------------------------------------------------------------------------------------------
     Reverse     |   2000   |                    |                    |      
     Reverse     |   3000   |                    |                    |     
     Reverse     |   4000   |                    |                    |     
     Reverse     |   5000   |                    |                    |    
------------------------------------------------------------------------------------------
Move front to end|   2000   |                    |                    |    
Move front to end|   3000   |                    |                    |    
Move front to end|   4000   |                    |                    |     
Move front to end|   5000   |                    |                    |     
------------------------------------------------------------------------------------------
Move end to front|   2000   |                    |                    |     
Move end to front|   3000   |                    |                    |     
Move end to front|   4000   |                    |                    |     
Move end to front|   5000   |                    |                    |    
Move end to front|   6000   |                    |                    |
'''












    