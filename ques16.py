# 16. Write a Python program to sum all the items in a list.

def list_sum(digit_list):
   sum = 0
   for digit in digit_list:
       sum += digit
   return sum
if __name__=="__main__":
   res = list_sum([2,3,5,6,7,8,4,3])
   print(res)
