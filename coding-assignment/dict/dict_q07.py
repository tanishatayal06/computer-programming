# Problem: Count the frequency of each element in a list using a dictionary.
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_dict = {}
for item in my_list:
    freq_dict[item] = freq_dict.get(item, 0) + 1
print(freq_dict)
