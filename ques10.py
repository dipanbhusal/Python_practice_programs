# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
def string_manipulation(string):
   result = string[0::2]
   return result
if __name__=="__main__":
  test_string = input('Enter the string: ')
  res = string_manipulation(test_string)
  print(res)
