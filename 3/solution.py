from collections import Counter

with open("input.txt") as f:
    inp = f.read()

locations = [(0,0)]


santa = [i for c, i in enumerate(inp) if c%2!=0]
robo = [i for c, i in enumerate(inp) if c%2==0]

def move(inp):
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

move(santa)
move(robo)

print(len(set(locations)))