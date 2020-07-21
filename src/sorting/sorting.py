# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    j = 0
    i = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] > arrB[j]:
            merged_arr.append(arrB.pop())
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    print(f'arrA:', arrA)
    print(f'arrB:', arrB)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # if the length of the array is 1
    if len(arr) > 1:
        # return array
        # midpoint
        midpoint = len(arr) // 2
        # left side
        a1 = arr[:midpoint]
        # right side
        a2 = arr[midpoint:]
        merge_sort(a1)
        merge_sort(a2)
        # print(a1)
    # print(a2)
    return merge(a1, a2)


testingArray = [87, 6, 2, 1, 4, 7, 54]
print(merge_sort(testingArray))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    return


def merge_sort_in_place(arr, l, r):
    # Your code here
    return
