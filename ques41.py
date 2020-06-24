# 41. Write a Python program to convert a tuple to a string.

sample_tuple = ('Ram', 'Khadka',20, 'TU')
modified_tuple = map(lambda x: str(x), sample_tuple)
result = ' '.join(list(modified_tuple))

print(result)