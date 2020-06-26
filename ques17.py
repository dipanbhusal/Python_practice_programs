# 17. Write a Python program to multiplies all the items in a list

def list_product(digit_list):
   product = 1
   for digit in digit_list:
       product *= digit
   return product
if __name__=="__main__":
   res = list_product([2,3,5,6])
   print(res)
