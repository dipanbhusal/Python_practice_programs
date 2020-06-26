# 22. Write a Python program to remove duplicates from a list.

def remove_duplicates_list(list_items):
   result = list(set(list_items))
   return result     
if __name__=="__main__":
   res = remove_duplicates_list([2,4,5,5,3,2,2,4,1,1,1])
   print(res)
