# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'

def frequency_count(string):
   result = {}
   for char in string:
       if char not in result:
           result[char] = string.count(char)
   print(result)
if __name__=="__main__":
   frequency_count('google.com')
