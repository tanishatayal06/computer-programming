# Problem: Write a function to count the frequency of each character in a string.
st = 'apple'
c = ''
for i in st:
    if i not in c:
        print(i,":",st.count(i), end=', ')
        c+=i
