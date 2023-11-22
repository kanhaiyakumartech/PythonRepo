def format_numbers(number):
    result = []
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        deci = str(i).rjust(width)
        octa = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        bina = bin(i)[2:].rjust(width)
        result.append((deci, octa, hexa, bina))
    return result
