from util import time_delta

def get_user_input():
    t = int(input("Enter: "))
    return [(input(), input()) for _ in range(t)]

if __name__ == '__main__':
    for t1, t2 in get_user_input():
        delta = time_delta(t1, t2)
        print(delta)
