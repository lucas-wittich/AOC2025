file = open('input.txt', 'r')
pos = 50
zeros = 0
for line in file:
    line = line.strip()

    direction = line[0]
    distance = int(line[1:])

    if direction == 'L':
        pos = (pos - distance) % 100
    else:
        pos = (pos + distance) % 100

    if pos == 0:
        zeros += 1

print(zeros)
