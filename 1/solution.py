with open("input.txt") as f:
    print(
        sum([1 if i == '(' else -1 for i in f.read()])
    )