file = open('input.txt', 'r')
pos = 50
zeros = 0
for line in file:
    line = line.strip()

    direction = line[0]
    distance = int(line[1:])

    if direction == 'L':
        step = -1
    else:
        step = 1

    for _ in range(distance):
        pos = (pos + step) % 100
        if pos == 0:
            zeros += 1

print(zeros)
