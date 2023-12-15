import numpy as np

# preamble
filename = "day1_input.txt"
data = np.loadtxt(filename, dtype=str)
sum_of_string = []
sum_of_each_strings = []

for i in range(len(data)):
    string = data[i]
    for char in string:
        if char.isnumeric():
            sum_of_string.append(int(char))
            sum_of_each_string = 0


# for char in string:
#     if char.isnumeric():
#         sum_of_string.append(int(char))


# number = [str(i) for i in sum_of_string]
# p = "".join(number)
# p = int(p)
# print(p)

def super_sum():
    pass