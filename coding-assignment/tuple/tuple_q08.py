# Write a python program to sort a tuple by its float element.
my_tuple = [(1, 20.5), (2, 10.0), (3, 15.5), (4, 5.5)]
sorted_tuple = sorted(my_tuple, key=lambda x: x[1])
print("Sorted tuple by float element:", sorted_tuple)
