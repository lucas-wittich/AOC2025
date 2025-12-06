file = open('input.txt', 'r')

lines = [line.split() for line in file]
ops = lines[4]
number_lines = lines[:4]
total = 0
a = 0
b = 0
c = 0
d = 0
for index in range(len(ops)):
    a = int(lines[0][index])
    b = int(lines[1][index])
    c = int(lines[2][index])
    d = int(lines[3][index])

    op = ops[index]
    if op == '+':
        val = a + b + c + d
    else:
        val = a * b * c * d

    total += val

print(total)
