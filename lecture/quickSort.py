# the partition function handles the work of selecting the pivot point
# selecting a pivot element and partitioning
# the data in the array around that pivot
# returns the left partition, the pivot, and the right partition
def partition(arr):
    # pick the first element as the pivot element
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, pivot, right


def quicksort(arr):
    # base case
    # if the length of the array is 0
    if len(arr) <= 1:
        return arr
    # how do we get closer to our base case?
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)


arr = [13, 27, 5, 18, 3, 19, 22, 16]

print(arr)
quicksort(arr)
print(quicksort(arr))
