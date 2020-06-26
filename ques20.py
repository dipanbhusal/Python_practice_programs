# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def string_count(string_list):
   count = 0
   for string in string_list:
       if len(string) >= 2:
           if string[0] == string[-1]:
               count += 1
   return count
if __name__=="__main__":
   res = string_count(['abc', 'xyz', 'aba', '1221'])
   print(res)
