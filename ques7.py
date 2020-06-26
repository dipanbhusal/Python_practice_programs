# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.

def string_manipulation():
   input_value = ''
   longest = 0
   while input_value != 'done':
       input_value = input('Enter the words: ')
       input_length = len(input_value)
       if longest <  input_length:
           longest = input_length
           longest_value = input_value 
   return (longest, longest_value)
 
if __name__=="__main__":
   length, value  = string_manipulation()
   print(f'The longest string: {value} with length {length}')
