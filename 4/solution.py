from hashlib import md5

with open("input.txt") as f:
    inp = f.read()


n = 0
ha = md5(f'{inp}{n}'.encode("utf-8"))

while ha.hexdigest()[0:5] != '00000':
    n += 1
    ha = md5(f'{inp}{n}'.encode("utf-8"))
print(n ,ha.hexdigest(), ha.hexdigest()[0:6])

print(n)