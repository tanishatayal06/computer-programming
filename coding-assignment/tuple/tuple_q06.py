# Write a python program to replace the last value of tuples in a list.
my_list = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
replace_num=int(input())
modified_list = [(t[:-1] + (replace_num,)) for t in my_list]
print("Modified list:", modified_list)
