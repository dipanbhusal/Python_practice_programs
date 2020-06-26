# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.

def insert_string(list_items, string):
   result_list = []
   for item in list_items:
       item = string + str(item)
       result_list.append(item)
   return result_list
      
if __name__=="__main__":
   main_list = [1,2,3,4]
   string = 'emp'
   res = insert_string(main_list, string)
   print(f'List: {main_list}\nString: {string}\nResult: {res}')
