# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

def string_manipulation(string):
   string_list = string.split(', ')
   result_list = []
   for one_string in string_list:
       if one_string not in result_list:
           result_list.append(one_string)
   result_list.sort()
   return result_list
 
if __name__=="__main__":
   test_string = input('Enter the string: ')
   res = string_manipulation(test_string)
   print(res)
