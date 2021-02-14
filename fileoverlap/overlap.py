"""Read two lists containing numbers and identify the overalpping numbers"""
happy_list = []
with open('happynumbers.txt','r') as h:
    line_happy = h.readline()
    while line_happy:
        happy_list.append(int(line_happy))
        line = h.readline()

prime_list = []
with open('primenumbers.txt','r') as p:
    line_prime = p.readline()
    while line_prime:
        prime_list.append(int(line_prime))
        line_prime = p.readline()
    
overlap_list = []
for i in happy_list:
    if i in prime_list:
        overlap_list.append(i)

print(overlap_list)