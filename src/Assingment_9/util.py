# util.py

import numpy as np

def find_max_of_min_values(matrix):
    # Convert the input list into a NumPy array
    my_array = np.array(matrix, dtype=int)

    # Find the minimum values along axis 1 (rows)
    min_values = np.min(my_array, axis=1)

    # Find the maximum of the minimum values
    result_max = np.max(min_values)

    return result_max
