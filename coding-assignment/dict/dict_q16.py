# Problem: Merge two dictionaries and combine the values of identical keys into a list.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'd': 6}
merged_dict = {}
for d in (dict1, dict2):
    for key, value in d.items():
        merged_dict.setdefault(key, []).append(value)

print(merged_dict)
