
from collections import deque


file = open('input.txt', 'r')
grid = [line.strip() for line in file]
file.close()

num_rows = len(grid)
num_cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0),  (1, 1),
]

removed_count = 0
degrees = [[0] * num_cols for _ in range(num_rows)]
present = [[False] * num_cols for _ in range(num_cols)]

for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] == '@':
            present[i][j] = True

for i in range(num_rows):
    for j in range(num_cols):
        if not present[i][j]:
            continue
        count = 0

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if 0 <= ni < num_rows and 0 <= nj < num_cols and present[ni][nj]:
                count += 1

        degrees[i][j] += count

q = deque()
for i in range(num_rows):
    for j in range(num_cols):
        if present[i][j] and degrees[i][j] < 4:
            q.append((i, j))

while q:
    i, j = q.popleft()
    if not present[i][j]:
        continue
    if grid[i][j] != '@':
        continue

    present[i][j] = False
    removed_count += 1

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < num_rows and 0 <= nj < num_cols:
            if present[ni][nj] and grid[ni][nj] == '@':
                degrees[ni][nj] -= 1
                # If this neighbor becomes removable, enqueue it
                if degrees[ni][nj] < 4:
                    q.append((ni, nj))

print(removed_count)
