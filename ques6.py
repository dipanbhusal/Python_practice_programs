# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.


def string_manipulation(string):
   if 'poor' and 'not' in string:
       poor_index = string.find('poor')
       not_index = string.find('not')
       if poor_index > not_index:
           result = string.replace(string[not_index:poor_index+4], 'good')     
   else:
       result = string
   return result 
if __name__=="__main__":
   test_string = input('Enter the string: ')
   res = string_manipulation(test_string)
   print(res)
