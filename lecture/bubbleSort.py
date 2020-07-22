def bubble_sort(arr):
    # iterating through the arr and look at elements two at a time
    # we know all the elements are in sorted order when we do a full pass thru the array and perfom no swaps
    swaps_occured = True
    while swaps_occured:
        swaps_occured = False

    # toggle swaps_occured boolean to False
    # if we do this all th eway thru all the elements will eventually end up in sorted order
    for i in range(len(arr) - 1):
        # we need to swap if arr[i] > arr[i + 1]
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swaps_occured = True
    return arr


def recursive_bubble_sort(arr, unsorted_length):
    # base case(s)
    # re - use the swaps_occured boolean idea
    # the boolean tells us when the 'unsorted' portion of the lsit reaches 0
    # if the length of the unsorted portion is 0
    # how do we get closer to a base case?
    # each pass shortens the unsorted portion by 1
    # each pass does what it did as what happened in the itterative case.

    for i in range(unsorted_length-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length-1)


arr = [5, 1, 7, 6, 2, 0]
print(arr)
recursive_bubble_sort(arr, len(arr))
print(arr)
