def repeated_twice(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


total = 0
file = open('input.txt', 'r')
for line in file:
    line = line.strip().split(',')

    for r in line:
        if not r:
            continue
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        for n in range(start, end + 1):
            if repeated_twice(n):
                total += n


print(total)
