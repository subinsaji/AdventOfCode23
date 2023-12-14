import numpy as np

filename = "day1_input.txt"
data = np.loadtxt(filename, dtype=str)

string =  data[1]
sum_of_string = []

for char in string:
    if char.isnumeric():
        sum_of_string.append(int(char))

number = [str(i) for i in sum_of_string]
p = "".join(number)
p = int(p)
print(p)



