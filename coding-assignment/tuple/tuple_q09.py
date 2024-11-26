# Write apython program to count the elements in a list until an element is a tuple.
my_list = [1, 2, 3, (4, 5), 6, 7]
count = 0
for item in my_list:
    if isinstance(item, tuple):  
        break  
    count += 1  
print("Number of elements before the tuple:", count)
