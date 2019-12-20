# STRETCH: implement Linear Search
def linear_search(arr, target):
    # Examine each element of arr from the beginning until a match to target is found
    for index, element in enumerate(arr):
        if element == target:
            return index
    # If no match found, return -1
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # arr empty

    low = 0
    high = len(arr)-1

    # Look for the target element in the middle of the current span
    # At the beginning of the search, the span will be the entire list

    while low <= high:
        # Calculate mid-point of current span and read the element at that location
        middle = (high + low) // 2
        element = arr[middle]

        # If the currently examined element is less than the target,
        # any potential match would have to be in the upper portion of the span,
        # so set a new span ranging from the midpoint as the lower bounds
        # to the end
        if element < target:
            low = middle + 1
        # If the currently examined element is greater than the target,
        # any potential match would have to be in the lower portion of the span,
        # so set a new span ranging from the beginning of the span as the lower bounds
        # to the middle
        elif element > target:
            high = middle - 1
        else:
            return middle

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0 or high < low:
        return -1  # array empty or no match found

    middle = (low+high)//2
    element = arr[middle]

    if element > target:
        return binary_search_recursive(arr, target, low, middle - 1)
    elif element < target:
        return binary_search_recursive(arr, target, middle + 1, high)
    else:
        return middle
