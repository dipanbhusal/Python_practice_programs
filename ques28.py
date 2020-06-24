# 28. Write a Python script to add a key to a dictionary.
def add_key(dictationary):
    sample_dict =  {0: 10, 1: 20}
    sample_dict.update(dictationary)
    print(sample_dict)

if __name__ == '__main__':
    add_key({2:30})