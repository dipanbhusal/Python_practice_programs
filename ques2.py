# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

def string_manipulation(string):
   if len(string) >= 2:
       result = string[0:2] + string[-2:]
   else:
       result = ""
   return result
if __name__=="__main__":
   test_string = input('Enter the string: ')
   res = string_manipulation(test_string)
   print(res)
