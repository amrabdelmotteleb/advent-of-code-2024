from itertools import combinations
from collections import defaultdict, deque

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()

tm = []
for line in data.split("\n"):
    line_lst = [int(num) for num in line]
    tm.append(line_lst)

R = len(tm)
C = len(tm[0])

# 1=up, 2=right, 3=down, 4=left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# P1

for r in range(R):
    for c in range(C):
        if tm[r][c] == 0:
            Q = deque([(0, r, c)])
            obs = set()
            while Q:
                val, cr, cc = Q.popleft()
                if (cr, cc) in obs:
                    continue

                obs.add((cr, cc))
                if tm[cr][cc] == 9:
                    p1_ans += 1
                    continue

                for (dr, dc) in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0<=nr<R and 0<=nc<C and tm[nr][nc] == val + 1:
                        Q.append((val+1, nr, nc))


# P2
for r in range(R):
    for c in range(C):
        if tm[r][c] == 0:
            Q = deque([(0, r, c, ((r,c), ))])
            obs = set()
            while Q:
                val, cr, cc, path = Q.popleft()
                if path in obs:
                    continue

                obs.add(path)
                if tm[cr][cc] == 9:
                    p2_ans += 1
                    continue

                for (dr, dc) in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0<=nr<R and 0<=nc<C and tm[nr][nc] == val + 1:
                        Q.append((val+1, nr, nc, path + ((nr, nc), )))


print(p1_ans)
print(p2_ans)
