# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

def string_swap(string1, string2):
  
   modified_str1 = string2[0:2]+string1[2:]
   modified_str2 = string1[0:2] + string2[2:]
   result = modified_str1 + ' '  + modified_str2
   return result
if __name__=="__main__":
   test_string1 = input('Enter the first string: ')
   test_string2 = input('Enter the second string: ')
   res = string_swap(test_string1, test_string2)
   print(res)
