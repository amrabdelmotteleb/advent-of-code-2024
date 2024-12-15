from collections import defaultdict, deque

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()

before_nums = defaultdict(set)
after_nums = defaultdict(set)

rules, updates = data.split("\n\n")

for rule in rules.split("\n"):
    x, y = rule.split("|")
    x, y = int(x), int(y)
    before_nums[y].add(x)
    after_nums[x].add(y)

for update in updates.split("\n"):
    update = [int(num) for num in update.split(",")]
    passes = True
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i<j and y in before_nums[x]:
                passes = False

    if passes:
        p1_ans += update[len(update) // 2]
    else:
        reordered_update = []
        Q = deque([])
        count_before_nums = {num: len(before_nums[num] & set(update)) for num in update}
        for num in update:
            if count_before_nums[num] == 0:
                Q.append(num)

        while Q:
            cur_num = Q.popleft()
            reordered_update.append(cur_num)
            for num in after_nums[cur_num]:
                if num in count_before_nums:
                    count_before_nums[num] -= 1
                    if count_before_nums[num] == 0:
                        Q.append(num)
        p2_ans += reordered_update[len(reordered_update) // 2]

print(p1_ans)
print(p2_ans)

