# 14. Write a Python function to create the HTML string with tags around the
# word(s).

def add_tag(tag,string):
   result = f'<{tag}>' + string + f'</{tag}>'
   return result
if __name__=="__main__":
   test_tag = input('Enter the tag: ')
   test_string = input('Enter the string: ')
   res = add_tag(test_tag,test_string)
   print(res)

