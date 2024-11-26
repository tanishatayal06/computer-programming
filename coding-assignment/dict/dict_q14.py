# Problem: Remove duplicate values from a dictionary, keeping only the first occurrence of each value.
my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print(unique_dict)
