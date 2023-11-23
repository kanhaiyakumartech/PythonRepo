#
if __name__ == '__main__':
# here we are taking size of list and stored in side n variavbles.
    n = int(input("Elter the Size of list = "))
# now map(int, ...) converts each substring to an integer.
    arr = map(int, input("Enter the value with space = ").split())
#set(arr): It converts the list arr into a set, removing any duplicate values.
#sorted(...): It sorts the unique values in ascending order.
#[-2]: It selects the second-to-last element in the sorted list, which is the second largest element.
    print(sorted(set(arr))[-2])
