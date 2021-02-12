"""Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file,
 and print out the results to the screen"""
 
counter = {}
with open('names.txt','r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter: 
            counter[line] += 1
        else:
            counter[line] = 1
        line = f.readline()
print(counter)