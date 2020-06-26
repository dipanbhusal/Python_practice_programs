# 1. Write a Python function to find the Max of three numbers.
def max_of_three_numbers(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'{num1} is max among 3 numbers.')
    elif num2 > num1 and  num2 > num3:
        print(f'{num2} is max among 3 numbers.')
    else: 
        print(f'{num3} is max among 3 numbers.')

max_of_three_numbers(43,65,31)

# 2. Write a Python function to sum all the numbers in a list.
from functools import reduce
def sum_of_all_numbers(given_list):
    result_sum = reduce(lambda x , y : x + y , given_list)
    return result_sum 

res =  sum_of_all_numbers([3,5,6,2,57,12])
print(f'Sum: {res}')

# 3. Write a Python function to multiply all the numbers in a list.
from functools import reduce

def product_of_all_numbers(given_list):
    result_product = reduce(lambda x, y:x * y , given_list)
    return result_product 

res =  product_of_all_numbers([8, 2, 3, -1, 7])
print(f'Product: {res}')

# 4. Write a Python program to reverse a string.
def reverse_string(string):
    return string[::-1]

print(reverse_string("1234abcd"))

# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))

# 6. Write a Python function to check whether a number is in a given range.
def check_within_range(number,range_from, range_to):
    if number in range(range_from, range_to):
        return True
    else:
        return False 
print(check_within_range(5, 0,9))

# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

def calculate_number_of_cases(string):
    uppercase_number = 0
    lowercase_number = 0
    for char in string:
        if char.isupper():
            uppercase_number += 1
        if char.islower():
            lowercase_number += 1
    return(uppercase_number, lowercase_number)

uppercase, lowercase = calculate_number_of_cases('The quick Brow Fox')
print(f'Number of uppercase letters: {uppercase}\nNumber of lowercase letters: {lowercase}')

# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def return_unique_list(given_list):
    result = list(set(given_list))
    return result
sample_list = [1,2,3,3,3,3,4,5] 
print(f'Sample_list: {sample_list}')
print(f'Unique List: {return_unique_list([1,2,3,3,3,3,4,5])}')

# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def check_prime(number):
    
    if number <= 1:
        return False
    for i in range(3,number//2):
        if number % i == 0:
            return False
            
    return True

print(check_prime(97))

# 10. Write a Python program to print the even numbers from a given list. 
def even_list(given_list):
    result = [n for n in given_list if n % 2==0]
    return result

res = even_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(res)

# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

first_lambda_function = lambda x: x + 15
second_lambda_function = lambda x, y: x * y 
print(first_lambda_function(4))
print(second_lambda_function(3,7))

# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.
def multiplicate_function(x):
    return lambda unknown_num : x * unknown_num

result = multiplicate_function(4)
print(f'The result is: {result(5)}') 

# 13. Write a Python program to sort a list of tuples using Lambda.
lambda_sort_tuples = lambda tuples : sorted(tuples , key=lambda tup: tup[-1:])
gvn_list = [(2,3),(4,1),(8,9),(2,0)]

print(f'The given tuples are: {gvn_list}')
print(f'The sorted tuples are: {lambda_sort_tuples(gvn_list)}')

# 14. Write a Python program to sort a list of dictionaries using Lambda.
list_dict = [{'name': 'Dipan', 'roll': 6}, {'name':'Python', 'roll': 3}, {'name':'MAc', 'roll':  1}, {'name':'Tom', 'roll': 2}]
lambda_sort_dict = lambda dicts: sorted(dicts, key=lambda x: x['roll'])

print(f'The given dicts are: {list_dict}')
print(f'The sorted dicts are: {lambda_sort_dict(list_dict)}')


# 15. Write a Python program to filter a list of integers using Lambda.

gvn_list = [4,6,1,3,7,9,4]
lambda_integer_filter = lambda list: filter(lambda y: y > 5, list)

print(f'The given list: {gvn_list}')
print(f'The filtered list having number greater than 5: {list(lambda_integer_filter(gvn_list))}')


# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.

gvn_list = [3,5,10,2,6]
lambda_square_list = map(lambda x: x ** 2, gvn_list)
lambda_cube_list = map(lambda x: x ** 3, gvn_list)

print(f'The square of list: {list(lambda_square_list)} ')
print(f'The cube of list: {list(lambda_cube_list)} ')


# 17. Write a Python program to find if a given string starts with a given character using Lambda.
string_starts_with = lambda char, string: True if string.startswith(char) else False 

print(string_starts_with('a','apple'))

# 18. Write a Python program to check whether a given string is number or not using Lambda.

is_number= lambda string: True if string.isdigit() else False 
print(is_number('111'))

# 19. Write a Python program to create Fibonacci series upto n using Lambda.
fibonacci = lambda num: 0 if num == 0 else (1 if num == 1 else fibonacci(num - 1) + fibonacci(num - 2) ) 
print(fibonacci(9))

# 20. Write a Python program to find intersection of two given arrays using Lambda.
list1 = [4,3,6,2,1]
list2 = [2,7,4,8]

intersection = lambda list1, list2: [x for x in list1 if x in list2]
print(intersection(list1, list2))