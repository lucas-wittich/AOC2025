def max_joltage(line):
    line = line.strip()

    digits = [int(ch) for ch in line]
    n = len(digits)

    suffix_max = [0] * n
    suffix_max[-1] = digits[-1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(digits[i], suffix_max[i + 1])

    best = 0

    for i in range(n - 1):
        second = suffix_max[i + 1]
        value = 10 * digits[i] + second
        if value > best:
            best = value

    return best


total = 0
file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    if not line:
        continue
    total += max_joltage(line)

print(total)
