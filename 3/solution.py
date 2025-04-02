from collections import Counter

with open("input.txt") as f:
    inp = f.read()

locations = [(0,0)]
x,y = 0, 0

for i in inp:
    if i == '>':
        x+=1
    elif i == '<':
        x-=1
    elif i == '^':
        y-=1
    elif i == 'v':
        y+=1

    locations.append((x,y))

print(len(set(locations)))