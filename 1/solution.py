with open("input.txt") as f:
    floors = [1 if i == '(' else -1 for i in f.read()]
    print(floors)

    floor = 0
    position = 0

    while floor >= 0:
        floor += floors[position]
        position += 1
        
    print(position)