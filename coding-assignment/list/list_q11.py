#  Problem: Convert the Given List into Nested List in Python
Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
		'Geeks, 123', '555.7492, 152.5406']
temp = []
for elem in Input:
	temp2 = elem.split(', ')
	temp.append((temp2))
Output = []
for elem in temp:
	temp3 = []
	for elem2 in elem:
		temp3.append(elem2)
	Output.append(temp3)
print(Output)
