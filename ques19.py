# 19. Write a Python program to get the smallest number from a list.

def smallest_in_list(digit_list):
   largest_number = digit_list[0]
   for digit in digit_list:
       if largest_number > digit:
           largest_number = digit 
   return largest_number
if __name__=="__main__":
   res = smallest_in_list([2,3,5,6,43,211,55,21,45,211,90])
   print(res)
