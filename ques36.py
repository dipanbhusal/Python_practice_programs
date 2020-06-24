# 36. Write a Python program to sum all the items in a dictionary.
dict1 =  {1:3, 2:7, 9:10, 8:2}
sum_items = 0
for value in dict1.values():
    sum_items+=value
print(sum_items)