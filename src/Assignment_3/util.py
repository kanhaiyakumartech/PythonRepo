# util.py
def second_largest_element(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]
