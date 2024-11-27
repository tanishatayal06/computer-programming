#  Problem: Using List Comprehension to Flatten a List of Lists
res = [i for row in [[1,3,"geeks"], [4,5], [6,"best"]] for i in row]
print(res)
