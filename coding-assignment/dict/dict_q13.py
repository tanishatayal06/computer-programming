# Problem: Check if one dictionary is a subset of another.
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2, 'c': 3}
is_subset = dict1.items() <= dict2.items()
print(is_subset)
