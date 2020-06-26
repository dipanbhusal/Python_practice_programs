# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.

def tuple_sort(tuple_list):
   result = sorted(tuple_list, key = lambda tuples: tuples[-1])
   return result
      
if __name__=="__main__":
   res = tuple_sort([(2, 1), (1, 2), (2, 3), (4, 4), (2, 5), (3,3)])
   print(res)
