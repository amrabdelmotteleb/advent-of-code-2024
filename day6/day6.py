# from collections import defaultdict, deque
from turtledemo.sorting_animate import start_isort

import numpy as np

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()
adv_map = data.split("\n")

# Contains tuples of indices that the agent has visited
ids_visited = set()

# # up, right, down, left
# dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

symbols_directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

flip_90 = {
    ">": "v",
    "v": "<",
    "<": "^",
    "^": ">"
}

# Find idx of agent
found_symbol = False
start_rc, start_symbol = None, None
cur_symbol = None
for i, line in enumerate(adv_map):
    if any(symbol in line for symbol in list(symbols_directions.keys())):
        for j, inp in enumerate(line):
            if inp == "^":
                start_rc, start_symbol = (i, j), inp
                ids_visited.add(start_rc)
                break

    if start_rc and start_symbol:
        found_symbol = True
        break

# P1
# Ensure that we have found the starting point
if found_symbol:
    start_i, start_j = next(iter(ids_visited))
    cur_symbol = start_symbol
    i_step, j_step = symbols_directions[cur_symbol][0], symbols_directions[cur_symbol][1]

    nxt_i = start_i + i_step
    nxt_j = start_j + j_step

    while 0 <= nxt_i < len(adv_map) and 0 <= nxt_j < len(adv_map[0]):
            if adv_map[nxt_i][nxt_j] == ".":
                # Advance to the next step
                ids_visited.add((nxt_i, nxt_j))
                i_step, j_step = symbols_directions[cur_symbol][0], symbols_directions[cur_symbol][1]
                nxt_i = nxt_i + i_step
                nxt_j = nxt_j + j_step
            else:
                # Flip the symbol by 90 degrees
                cur_symbol = flip_90[cur_symbol]
                old_i_step, old_j_step = i_step, j_step
                i_step, j_step = symbols_directions[cur_symbol][0], symbols_directions[cur_symbol][1]
                # Move it back, then progress in the right direction
                nxt_i = nxt_i - old_i_step + i_step
                nxt_j = nxt_j - old_j_step + j_step

    p1_ans = len(ids_visited)

# P2
# 0=up, 1=right, 2=down, 3=left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
num_r = len(adv_map)
num_c = len(adv_map[0])
for id in ids_visited:
        itr_r, itr_c = id
        r, c = start_rc[0], start_rc[1]
        # We know that the starting point is pointing upwards
        d = 0
        seen = set()
        while True:
            if (r, c, d) in seen:
                # found a loop
                p2_ans += 1
                break
            seen.add((r, c, d))
            dr, dc = dirs[d]
            new_r = r + dr
            new_c = c + dc
            if not (0<=new_r<num_r and 0<=new_c<num_c):
                break

            if adv_map[new_r][new_c] == "#" or new_r == itr_r and new_c == itr_c:
                # If the condition after the "or" is true, then we'd try adding a "#" there
                # This would either create a loop, or it will not, hence we'd reach to a point where we go out
                # of our boundaries
                d = (d+1)%4

            else:
                r = new_r
                c = new_c

print(p1_ans)
print(p2_ans)



