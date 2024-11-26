# Write a python program to check whether an element exist whithin a tuple.
my_tuple = (10, 20, 30, 40, 50)
element = int(input())
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
