K = 12


def max_k_digit_subsequence(num_str: str, k: int) -> str:

    num_str = num_str.strip()
    n = len(num_str)
    if n <= k:
        return num_str

    to_remove = n - k
    stack = []

    for ch in num_str:
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    # If we still have digits to remove, remove from the end
    if to_remove > 0:
        stack = stack[:-to_remove]

    # Take exactly k digits
    return ''.join(stack[:k])


total = 0
file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    if not line:
        continue

    best = max_k_digit_subsequence(line, K)
    total += int(best)
print(total)
