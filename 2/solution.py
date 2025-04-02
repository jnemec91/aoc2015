with open("input.txt") as f:
    input = f.read().split()


def calculate(l,w,h):
    sides = [
        2*(l*w),
        2*(w*h),
        2*(h*l)
    ]
    return sum(sides) + int(min(sides)/2)

total = 0
for i in input:
    dim = [int(j) for j in i.split('x')]
    total += calculate(*dim)

print(total)