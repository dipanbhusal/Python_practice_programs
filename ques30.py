# 30. Write a Python script to check whether a given key already exists in a dictionary.

gvn_key = 10
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
count = 0
for key in sample_dict:
    if key == gvn_key:
        count = 1
if count == 1:
    print('Given key exists.')
else:
    print("Given key doesn't exists.") 