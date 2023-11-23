# Here i declered a Function
def second_largest_element(arr):
#set(arr): It converts the list arr into a set, removing any duplicate values.
#sorted(...): It sorts the unique values in ascending order.
#[-2]: It selects the second-to-last element in the sorted list, which is the second largest element.
    arr = list(set(arr))
    arr.sort()
    return arr[-2]
