# 37. Write a Python program to multiply all the items in a dictionary.

dict1 =  {1:3, 2:7, 9:10, 8:2}
product_items = 1
for value in dict1.values():
    product_items *= value 
print(product_items)