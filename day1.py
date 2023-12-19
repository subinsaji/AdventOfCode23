import numpy as np
import re

digits_array = np.array([])

with open("day1_input.txt", "r") as file:
    for line in file:
        first_digit_match = re.search(r"\d", line)
        if first_digit_match:
            first_digit = first_digit_match.group()
        else:
            continue

        last_digit_match = re.search(r"\d(?=[^\d]*$)", line)
        if last_digit_match:
            last_digit = last_digit_match.group()
        else:
            continue

        combined_number = int(first_digit + last_digit)
        digits_array = np.append(digits_array, combined_number)

array_sum = np.sum(digits_array)
print(array_sum)

