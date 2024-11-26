# Problem: Write a function to find the longest word in a given sentence.
string1 = input("enter the string: ")
word = string1.split()
largest = word[0]
for i in range(len(word)):
  if len(largest) < len(word[i]):
    largest = word[i]
     print("largest word is ",largest)

