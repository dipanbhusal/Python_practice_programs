# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.


def string_adding(string):
   if len(string) >= 3:
       if string[-3:] =='ing':
           result = string + 'ly'
       else:
           result = string + 'ing'
   else:
       result = string
   return result
if __name__=="__main__":
   test_string = input('Enter the string: ')
   res = string_adding(test_string)
   print(res)
