# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.

def check_dict_empty(list_items):
   count = 0
   for item in list_items:
       if not item:
           count +=  1 
   if count == len(list_items):
       return True
   else:
       return False
      
if __name__=="__main__":
   main_list = [{},{},{1:4}]
   res = check_dict_empty(main_list)
   print(res)
