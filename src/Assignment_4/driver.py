from src.Assignment_4.util import My_mutate_string
if __name__ == '__main__':
    s = input("Enter the String = ")
    i, c = input("Enter the index value and change latter = ").split()
    s_new = My_mutate_string(s, int(i), c)
    print(s_new)
