# 15. Write a Python function to insert a string in the middle of a string.


def insert_string_middle(string1,string2):
   mid = len(string1) //2
   result = string1[0:mid] + string2 + string1[mid:]
 
   return result
if __name__=="__main__":
   test_string1 = input('Enter the string1: ')
   test_string2 = input('Enter the string1: ')
   res = insert_string_middle(test_string1,test_string2)
   print(res)
