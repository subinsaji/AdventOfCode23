import numpy as np

filename = "day1_input.txt"
data = np.loadtxt(filename, dtype=str)
number_in_string = []
first = True

for i in range(len(data)):
    join_number_in_string = [number_in_string[j] for j in number_in_string]
    p = "".join(join_number_in_string)
    #p = int(p)

    sum_of_string = sum(p)
    string = data[i]
    for char in string:
        if char.isnumeric():
            number_in_string.append(int(char))

    



# def joining_function(join_number_string):
#     join_number_in_string = [number_in_string[j] for j in number_in_string]
#     p = "".join(join_number_in_string)
#     p = int(p)
#     p = np.array(p)
#     print(p)
#     return p




# number = [str(i) for i in number_in_string]
# p = "".join(number)
# p = int(p)
# print(p)

# def add_numbers():
#     number = [str(i) for i in sum]
#     pass


# def super_adder():
#     pass