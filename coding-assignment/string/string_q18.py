# Problem: Implement basic string compression using the counts of repeated characters.
input_string = input()
compressed = []
count = 1
for i in range(1, len(input_string)):
    if input_string[i] == input_string[i-1]:
        count += 1
    else:
        compressed.append(input_string[i-1] + str(count))
        count = 1
compressed.append(input_string[-1] + str(count))
compressed_string = "".join(compressed)
print(compressed_string if len(compressed_string) < len(input_string) else input_string)

