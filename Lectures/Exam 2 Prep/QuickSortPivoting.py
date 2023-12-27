def quicksort(L, partition):
    """Sorts L using quicksort. Best case: O(nlogn); worst case: O(n^2)"""

    def _quicksort(L, left, right):
        """Helper function for quicksort"""
        if right-left<=1: return


        pivot = partition(L, left, right)

        _quicksort(L, left, pivot )
        _quicksort(L, pivot+1, right)


    _quicksort(L, left=0, right=len(L))


def partition_last(L, left,right):
    i, j, pivot= left, right-2, right -1

    while i < j:
        while L[i] < L[pivot]: i += 1
        while i < j and L[j] >= L[pivot]: j-= 1
        if i < j: L[i], L[j] = L[j], L[i]


    if L[pivot] <= L[i]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    return pivot

def partition_random(L, left, right):
    """Partitions with random element as pivot"""