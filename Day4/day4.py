
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

count = 0

for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] != '@':
            continue

        neighbor_cnt = 0

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if 0 <= ni < num_rows and 0 <= nj < num_cols:
                if grid[ni][nj] == '@':
                    neighbor_cnt += 1

        if neighbor_cnt < 4:
            count += 1

print(count)
