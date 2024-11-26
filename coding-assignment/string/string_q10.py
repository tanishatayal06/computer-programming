# Problem: Write a function to reverse each word in a sentence.
input_string = input()
words = input_string.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))

