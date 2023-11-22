if __name__ == '__main__':
    n = int(input("Elter the Size of list = "))
    arr = map(int, input("Enter the value with space = ").split())
    print(sorted(set(arr))[-2])
