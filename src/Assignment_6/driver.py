# driver.py
#In this we used a collection of datatypes python known as an ordered dictionary.
#Ordered dictionary Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.
#It also removes all the repeatations in the string.
#Also in the top lines we have used string slicing to slice strings based on the parts needed.
from util import merge_the_tools

if __name__ == '__main__':
    string, k = input("Enter the String Value= "), int(input("Enter the Key Value= "))
    result = list(merge_the_tools(string, k))
    for word in result:
        print(word)
