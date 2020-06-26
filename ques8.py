# 8. Write a python program to remove the nth index character from nonempty string. 

 
def string_manipulation(string, index ):
   result = string.replace(string[index-1], '')
   return result
if __name__=="__main__":
   test_string = input('Enter the string: ')
   index =int(input('Enter the index of character: '))
   res = string_manipulation(test_string, index)
   print(res)
