# Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an string No common"".
strs = input().split()
if not strs:
    print("No common")
else:
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                print("")
                exit()
    print(prefix)
