#Find multiples of 3 and 5 below 1000 and find the sum of that multiple
multiples = []
total = 0
def find_multiples():
    a = range(1,1000)
    for i in a:
        if i%3 == 0 or i%5 == 0:
            multiples.append(i)
find_multiples()

for ele in range(0, len(multiples)):
    total = total + multiples[ele]
      

print("The sum of elements is:", total)

""" Better Answer
L=[i for i in range(1000) if i%3==0 or i%5==0]
print(sum(L))
"""