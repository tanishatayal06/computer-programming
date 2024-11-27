# Problem: Write a python program to check whether two lists are circularly identical
list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]
if len(list1) == len(list2) and list2 in (list1 + list1):
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")

