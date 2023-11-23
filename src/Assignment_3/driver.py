# Thi scode for find the 2nd Greatest no in list .
from util import second_largest_element

if __name__ == '__main__':
# here we are taking size of list and stored in side n variavbles.

    n = int(input("Enter the number of elements: "))

# now map(int, ...) converts each substring to an integer.

    arr = map(int, input("Enter the elements separated by space: ").split())
    result = second_largest_element(arr)
    print(f"The second largest element is: {result}")
