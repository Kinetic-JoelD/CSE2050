from math import log2
import random

###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def linear_scan(L): 
    """
    A function that does a single linear scan of a list L and returns an 
    integer denoting which case that lists fits into (return value will be one of {0, 1, 2, 3})
    """

    # Counts how many items are out of place
    unords = 0
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            unords += 1

    # Edge case with an empty list
    if len(L) == 0:
        return 0

    # If the list is already sorted
    elif unords == 0:
        return 1
    
    # List is reverse sorted
    elif unords == len(L) - 1:
        return 3

    # List has a small amount of unordered stuff
    elif unords <= 10:
        return 2

    # None of the above cases applied
    else:
        return 0
    
def reverse_list(L):
    """
    Function that reverses a list efficientyly
    """
    # Finds the index of the end of a list
    end = len(L) - 1

    # Swapping each of the ends
    for i in range(len(L) // 2):
        L[i], L[end - i] = L[end - i], L[i]

def insertion_sort(L, left = 0, right = None): 
    """
    Builds the final sorted list one item at a time. Takes each element from the input list and 
    inserts it into its correct position within the sorted part of the list.
    """
    # No right input was given, so set right to the end of the list
    if right is None:
        right = len(L)

    # Insertion sort for the specified section of the list
    for i in range(left + 1, right):
        key = L[i]
        j = i - 1
        while j >= left and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

def quick_sort(L, left = 0, right = None, depth = 0):
    if right is None:
        right = len(L)

    # Check if the list is small enough for Merge Sort and if the depth limit is reached
    if right - left <= 1 or depth > 3 * (log2(right - left) + 1):
        merge_sort(L, left, right)
    else:
        # Choose the last element as the pivot
        pivot_index = right - 1
        pivot = L[pivot_index]

        # Initialize pointers
        i = left
        for j in range(left, pivot_index):
            if L[j] < pivot:
                L[i], L[j] = L[j], L[i]
                i += 1

        # Place the pivot in its correct position
        L[i], L[pivot_index] = L[pivot_index], L[i]

        # Recursively sort the two partitions
        quick_sort(L, left, i, depth + 1)
        quick_sort(L, i + 1, right, depth + 1)

def merge(A, B, L):
    # Creates two pointers, i for A and j for B
    i, j = 0, 0

    # Loop until we have iterated through both lists A and B
    while i < len(A) or j < len(B):
        # Compare the current elements of A and B, add the smaller one to the result list L
        if j == len(B) or (i < len(A) and A[i] < B[j]):
            L[i + j] = A[i]
            i = i + 1
        else:
            L[i + j] = B[j]
            j = j + 1

def merge_sort(L, left=0, right=None):

    # No right input was given, so set right to the end of the list
    if right is None:
        right = len(L)

    # If the sublist size is 20 or smaller, use insertion sort
    if right - left <= 20:
        insertion_sort(L, left, right)
    else:
        # Calculate the midpoint of the sublist
        mid = (left + right) // 2

        # Recursively sort the left and right halves using merge sort
        merge_sort(L, left, mid)
        merge_sort(L, mid, right)

        # Merge the two sorted halves back into a single sorted list
        merge(L, left, mid, right)

def magic_sort(L):
    """
    Creates a general purpose sorting algorithm made up of multiple different sorting algorithms O(n)
    """

    caseNum = linear_scan(L)

    # Runs the quicksort function for case 0
    if caseNum == 0:

        # For testing
        quick_sort(L)

    # Case 1: The list is already sorted
    elif caseNum == 1:
        return
    
    # Case 2: Calls insertion sort if the unordered stuff is less than 10 
    elif caseNum == 2:
        insertion_sort(L)

    # Case 3:  The list is reverse sorted
    elif caseNum == 3:
        merge_sort(L)