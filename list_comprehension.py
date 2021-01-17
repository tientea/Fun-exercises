import random
#Generate two random lists and find common numbers without duplicates
a = random.sample(range(1,20),12)
b = random.sample(range(1,20),15)
#sorting lists
a.sort()
b.sort()
print(a)
print(b)
#List comprehension, checking for dups by using dictionary properties and reverting
c = sorted(list(dict.fromkeys([aa for aa in a if aa in b])))
print(c)