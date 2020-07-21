testingArray = []
# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):
    # Your code here
    # find the midpoint and check to see if the target is equal to, greater than, or less than the mid area.if not split the next half in half and see if the target is less than, greater than or equal to it.
    midpoint = start + end // 2
    if arr[midpoint] == target:
        return midpoint
    if target < arr[midpoint]:
        binary_search(arr[midpoint:], target, midpoint, end)
    else:
        binary_search(arr[:midpoint], target, start, midpoint)
    return
    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    return
