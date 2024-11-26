# Problem: Flatten a nested dictionary where each value is another dictionary.
nested_dict = {'a': {'x': 1, 'y': 2},
    'b': {'z': 3, 'w': 4}}
flat_dict = {f"{outer_key}_{inner_key}": value for outer_key, inner_dict in nested_dict.items() for inner_key, value in inner_dict.items()}
print(flat_dict)
