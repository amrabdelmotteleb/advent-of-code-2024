from itertools import combinations
from collections import defaultdict, deque

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()


# P1
files = deque([])
dots = deque([])
id = 0
pos = 0

for i, c in enumerate(data):
    if i%2 == 0:
        for _ in range(int(c)):
            files.append((pos, id))
            pos += 1
        id+=1

    else:
        for _ in range(int(c)):
            dots.append(pos)
            pos += 1


compressed = []

i = 0
refilled_dots = deque([])

while dots[0] < files[-1][0]:
    refilled_dots.append((dots[0], files[-1][-1]))
    dots.popleft()
    files.pop()


combined = refilled_dots + files

for entry in combined:
    p1_ans += entry[0] * int(entry[1])

# P2
files = deque([])
dots = deque([])
id = 0
pos = 0

# Add the entries one by one
entries = []

for i, rep in enumerate(data):
    if i%2 == 0:
        # pos in this case would represent the starting position
        files.append((pos, id, int(rep)))
        for _ in range(int(rep)):
            entries.append(id)
            pos += 1
        id+=1

    else:
        dots.append((pos, int(rep)))
        for _ in range(int(rep)):
            entries.append(".")
            pos+=1

for (file_i, file_id, num_files) in reversed(files):
    for ind, (dots_i, num_dots) in enumerate(dots):
        if num_dots >= num_files and file_i > dots_i:
            for i in range(num_files):
                entries[dots_i + i] = file_id
                entries[file_i + i] = "."
            # Update the dots (if some of them are still left)
            dots[ind] = (dots_i + num_files, num_dots - num_files)
            break

for j, val in enumerate(entries):
    if val != ".":
        p2_ans += j * val

print(p1_ans)
print(p2_ans)
