# 24. Write a Python program to clone or copy a list.

def clone_list(list_item):
   clonned_list = list.copy(list_item)
   return clonned_list
      
if __name__=="__main__":
   main_list = [1,2,4,5]
   res = clone_list(main_list)
   print(f'original list: {main_list}\nClonned list: {res}')
