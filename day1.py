import numpy as np

filename = "day1_input.txt"
data = np.loadtxt(filename, dtype=str)
number_in_string = []

for i in range(len(data)):
    first = True

    
    join_number_in_string = [number_in_string[j] for j in number_in_string]

    if first:
        string = data[i]
        for char in string:
            if char.isnumeric():
                number_in_string.append(int(char))


# number = [str(i) for i in number_in_string]
# p = "".join(number)
# p = int(p)
# print(p)

# def add_numbers():
#     number = [str(i) for i in sum]
#     pass


# def super_adder():
#     pass