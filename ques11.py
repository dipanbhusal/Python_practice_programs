# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

def string_manipulation(string):
   word_list = string.split(' ')
   result_dict= {}
   for word in word_list:
       if  word not a in result_dict:
           result_dict[word] = word_list.count(word)
   return result_dict
if __name__=="__main__":
  test_string = input('Enter the string: ')
  res = string_manipulation(test_string)
  print(res)
