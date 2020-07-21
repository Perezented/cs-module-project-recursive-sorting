testingArray = []
# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):
    # Your code here
    # find the midpoint and check to see if the target is equal to, greater than, or less than the mid area.if not split the next half in half and see if the target is less than, greater than or equal to it.
    midpoint = (start + end) // 2
    # print(arr)
    if len(arr) == 1:
        return arr
        if target == arr[midpoint]:
            return midpoint
    if target == arr[-1]:
        return len(arr)-1
    elif target > arr[midpoint]:
        # print(arr[midpoint:])
        binary_search(arr[midpoint:], target, start, len(arr[midpoint:]))
    elif target < arr[midpoint]:
        # print(arr[:midpoint])
        binary_search(arr[:midpoint], target, start, len(arr[:midpoint]))

    # if len(arr) == 0:
    #     return -1
    # if len(arr) == 1:
    #     print(arr)
    # else:
    #     if arr[midpoint + 1] >= target:
    #         binary_search(arr[start: midpoint], target, start, midpoint)
    #     if arr[midpoint] < target:
    #         end = end - midpoint
    #         binary_search(arr[midpoint:end], target, midpoint, end)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    return
