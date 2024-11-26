# A group of friends is organizing a list of words for a spelling contest. To prepare, they want to sort the words based on their lengths, with the shortest word first
sen = "apple banana fig date"
sen1 = sen.split()
fin_sen = sorted(sen1,key=len)
print(" ".join(fin_sen))
