# 27. Write a Python program to replace the last element in a list with another list.

def replace_element(list1, list2):
    result = list1[:-1] + list2 
    return result        
if __name__=="__main__":
    list1 = [1, 3, 5, 7, 9, 10]
    list2 = [2, 4, 6, 8]
    res = replace_element(list1, list2)
    print(f'List1: {list1}\nList2: {list2}\nResult: {res}')

    