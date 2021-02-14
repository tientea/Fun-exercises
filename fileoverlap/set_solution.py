prime=open("primenumbers.txt").read().split("\n")
happy=open("happynumbers.txt").read().split("\n")

print(sorted(set(prime).intersection(set(happy))))

