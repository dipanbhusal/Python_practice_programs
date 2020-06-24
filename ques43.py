# 43. Write a Python program to remove an item from a tuple. 

sample_tuple = ('Ram', 'Khadka',20, 'TU')
item_to_remove = 'TU'

modified_tuple_to_list = list(sample_tuple)
modified_tuple_to_list.remove(item_to_remove)
result = tuple(modified_tuple_to_list)
print(result )