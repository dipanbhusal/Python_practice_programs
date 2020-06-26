# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.

def string_occurance(string):
   first_character = string[0]
   result = first_character +  ''
   for substring in string[1:]:
       if substring == first_character:
           substring = "$"
       result += substring
   return result
if __name__=="__main__":
   test_string = input('Enter the string: ')
   res = string_occurance(test_string)
   print(res)
