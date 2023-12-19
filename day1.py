import numpy as np
import re

filename = "day1_input.txt"
string_list = np.loadtxt(filename, dtype=str)

def sum_of_joined_digits(string_list):
    numbers  = []
    for s in string_list:
        number = "".join(re.findall(r"\d", s))
        if number:
            numbers.append(int(number))

    return sum(numbers)


print(sum_of_joined_digits(string_list))
