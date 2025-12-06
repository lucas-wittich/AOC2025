with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]

num_rows = lines[:-1]
ops_row = lines[-1]

height = len(num_rows)
width = len(num_rows[0])

total = 0
numbers = []
current_number_digits = []


def flush_number():
    if current_number_digits:
        n = int("".join(current_number_digits))
        numbers.append(n)
        current_number_digits.clear()


for col in reversed(range(width)):
    op = ops_row[col]

    column_is_blank = all(row[col] == " " for row in num_rows)

    if column_is_blank:
        flush_number()
        if numbers:
            op_symbol = last_op
            if op_symbol == '+':
                total += sum(numbers)
            else:
                prod = 1
                for n in numbers:
                    prod *= n
                total += prod
            numbers.clear()
        continue

    current_number_digits = [num_rows[r][col] for r in range(height)]
    flush_number()

    if op in "+*":
        last_op = op

if numbers:
    if last_op == "+":
        total += sum(numbers)
    else:
        prod = 1
        for n in numbers:
            prod *= n
        total += prod

print(total)
