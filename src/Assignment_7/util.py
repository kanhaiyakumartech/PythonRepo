# First we created a function. This function will take a number as input.
def format_numbers(number):
    result = []
# then, we created a variable.
    width = len(bin(number)[2:])
# then, we created a loop in the range 1 to num+1.
    for i in range(1, number + 1):
# then, we changed our i in binary, octal, decimal, and hexadecimal
        deci = str(i).rjust(width)
        octa = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        bina = bin(i)[2:].rjust(width)
        result.append((deci, octa, hexa, bina))
    return result
