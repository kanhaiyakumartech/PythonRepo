from util import format_numbers

if __name__ == '__main__':
    n = int(input("Enter any Number : "))
    formatted_numbers = format_numbers(n)
    for entry in formatted_numbers:
        print(" ".join(entry))
