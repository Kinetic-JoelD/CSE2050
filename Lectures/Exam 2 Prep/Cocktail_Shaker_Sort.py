def cock_tail_shaker(lst):
    left = 0
    right = len(lst) - 1
    swapped = True

    while swapped != False:
        swapped = False

        for i in range(left, right):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        
        right -= 1

        for i in range(right, left, -1):
            if lst[i] < lst[i-1]:
                lst[i], lst[i -1] = lst[i -1], lst[i]
                swapped = True

        left += 1
        print(lst)

    return lst


def cocktail_shaker_sort2(arr):
    left = 0
    right = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Left to right phase
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Shrink the range of unsorted elements from the right
        right -= 1

        # Right to left phase
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Shrink the range of unsorted elements from the left
        left += 1

    return arr


if __name__ == "__main__":
    mylst = [5, 2, 2, 2, 2, 2, 1]
    cock_tail_shaker(mylst)
    print(mylst)


