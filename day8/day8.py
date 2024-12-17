from itertools import combinations
from collections import defaultdict

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()


grid = data.split("\n")
R = len(grid)
C = len(grid[0])

grid_dict = defaultdict(set)
uniq_locs_p1 = set()

# Fill the grid dict
for r in range(R):
    for c in range(C):
        if grid[r][c] != ".":
            grid_dict[grid[r][c]].add((r,c))

for antenna, positions in grid_dict.items():
    pairs = list(combinations(positions, r=2))
    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = x1 - x2
        dy = y1 - y2

        a1x, a1y = 2*x1 - x2, 2*y1 - y2
        a2x, a2y = 2*x2 - x1, 2*y2 - y1

        # Check if the antennas are within the grid
        if 0<=a1x<R and 0<=a1y<C:
            uniq_locs_p1.add((a1x, a1y))
        if 0<=a2x<R and 0<=a2y<C:
            uniq_locs_p1.add((a2x, a2y))

if uniq_locs_p1:
    p1_ans = len(uniq_locs_p1)
    print(p1_ans)


# P2
uniq_locs_p2 = set()

for antenna, positions in grid_dict.items():
    pairs = list(combinations(positions, r=2))
    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = x1 - x2
        dy = y1 - y2

        # dir 1
        dirs = [1, -1]
        for dir_sign in dirs:
            i = 0
            while True:
                x_n = x2 + dir_sign * i * dx
                y_n = y2 + dir_sign * i * dy
                if 0 <= x_n < R and 0 <= y_n < C:
                    uniq_locs_p2.add((x_n, y_n))
                    i += 1
                else:
                    # We went off the grid
                    break


if uniq_locs_p2:
    p2_ans = len(uniq_locs_p2)
    print(p2_ans)