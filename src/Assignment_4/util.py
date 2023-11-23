# Here I Declered a Function and pass the Arguments.
def My_mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    return "".join(lst)
