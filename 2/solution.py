with open("input.txt") as f:
    input = f.read().split()


def calculate(l,w,h):
    dim = [l,w,h]
    a = dim.pop(dim.index(max(dim)))

    return sum([i*2 for i in dim])+(l*w*h)

total = 0
for i in input:
    dim = [int(j) for j in i.split('x')]
    total += calculate(*dim)

print(total)