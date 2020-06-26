# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.
 
def string_manipulation(string):
   upper_case = string.upper()
   lower_case = string.lower()
   return (upper_case, lower_case)
if __name__=="__main__":
  test_string = input('Enter the string: ')
  upper, lower = string_manipulation(test_string)
  print(f'Upper case: {upper}\nLower case: {lower}')

