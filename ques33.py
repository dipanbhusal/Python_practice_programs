# 33. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

given_num = 15
result_dict = {}
for index in range(1, given_num+1):
    result_dict[index] = index ** 2
print(result_dict)