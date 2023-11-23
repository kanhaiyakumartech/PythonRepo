
# This is celendra Program
from util import Check_Day_Name

if __name__ == '__main__':
    month, day, year = map(int, input("Enter month, day, and year (separated by space): ").split())
    result = Check_Day_Name(month, day, year)
    print(f"The day is: {result}")
    
