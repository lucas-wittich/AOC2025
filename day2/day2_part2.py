def repeated(n):
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k == 0:
            repeats = L // k
            if s == s[:k] * repeats:
                return True

    return False


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
            if repeated(n):
                total += n


print(total)
