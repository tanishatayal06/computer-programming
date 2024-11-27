# Problem: Python program to concatenate every elements across lists.
test_list1 = ["gfg", "is", "best"]
test_list2 = ["love", "CS"]
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
temp = [(a, b) for a in test_list1 for b in test_list2]
res = [x + ' ' + y for (x, y) in temp]
print("The paired combinations : " + str(res))
