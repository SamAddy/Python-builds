def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right, equal = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        elif num == pivot:
            equal.append(num)

    return quicksort(left) + equal + quicksort(right)


# Sorting in place and memory
def partition(arr, low, high):
    pivot = arr[0]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def quicksort2(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = partition(arr, low, high)
        quicksort2(arr, low, pivot)
        quicksort2(arr, pivot + 1, high)