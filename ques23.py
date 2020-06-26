# 23. Write a Python program to check a list is empty or not.

def check_list_is_empty(list_item):
   if  not  list_item:
       return True
   else:
       return False  
if __name__=="__main__":
   res = check_list_is_empty([])
   print(res)
