# Problem: Write a function to remove all digits from a string.
input_string = input()
result_string = "".join([char for char in input_string if not char.isdigit()])
print(result_string)
