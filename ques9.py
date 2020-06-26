# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def string_manipulation(string):
  result = string[-1] + string[1:-1] + string[0]
  return result
if __name__=="__main__":
  test_string = input('Enter the string: ')
  res = string_manipulation(test_string)
  print(res)
