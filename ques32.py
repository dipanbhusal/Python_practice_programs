# 32. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

given_n = 5
result_dict = {}
for num in range(1,given_n+1):
    result_dict[num]  = num * num 
print(result_dict)