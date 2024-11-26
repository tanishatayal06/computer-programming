# Write a python program to remove an empty tuples from a list of tuples
my_list = [(10, 20), (), (30, 40), (), (50,)]
filtered_list = [t for t in my_list if t]
print("List after removing empty tuples:", filtered_list)

