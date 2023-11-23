# driver.py

from util import find_max_of_min_values

def main():
    # Read the dimensions of the matrix
    M, N = map(int, input("Enter the dimensions of the matrix (M N): ").split())

    # Read the matrix
    matrix = [input(f"Enter row {i + 1} (space-separated values): ").split() for i in range(M)]

    # Call the user-defined function to find the result
    result = find_max_of_min_values(matrix)

    # Print the result
    print("Result:", result)

if __name__ == "__main__":
    main()
