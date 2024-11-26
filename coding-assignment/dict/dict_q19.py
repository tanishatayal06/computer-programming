# Problem: Get all keys in the dictionary that end with a specific suffix.
my_dict = {'file1.txt': 100, 'file2.txt': 200, 'image.jpg': 300}
suffix = '.txt'
keys_with_suffix = [k for k in my_dict.keys() if k.endswith(suffix)]
print(keys_with_suffix)
