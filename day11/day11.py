from collections import deque

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()
nums = [int(num) for num in data.split(" ")]

updated_nums = nums.copy()

num_blinks = 25
pos = 0

for _ in range(num_blinks):
    for num in nums:
        if num == 0:
            updated_nums[pos] = 1
            pos += 1
            continue

        l = len(str(num))
        if l % 2 == 0:
            stone1, stone2 = int(str(num)[:l//2]), int(str(num)[l//2:])
            updated_nums[pos] = stone1
            updated_nums.insert(pos+1, stone2)
            pos+=2
            continue

        updated_nums[pos]*=2024
        pos+=1

    # Update nums
    nums = updated_nums.copy()
    # Reset pos
    pos = 0

p1_ans = len(nums)

# P2
# update blinks
num_blinks = 75

def itr(s_val: int, b_itr: int):
    lng = len(str(s_val))
    if (s_val, b_itr) in seen:
        return seen[(s_val, b_itr)]

    if b_itr == num_blinks:
        return 0

    if s_val == 0:
        seen[(s_val, b_itr)] = itr(1, b_itr + 1)
        return seen[(s_val, b_itr)]

    if lng % 2 == 0:
        seen[(s_val, b_itr)] = 1 + itr(
            int(str(s_val)[:lng // 2]), b_itr + 1
        ) + itr(
            int(str(s_val)[lng // 2:]), b_itr + 1
        )
        return seen[(s_val, b_itr)]

    seen[(s_val, b_itr)] = itr(s_val * 2024, b_itr + 1)
    return seen[(s_val, b_itr)]


seen = dict()
nums = [(int(num), 0) for num in data.split(" ")]
stones = deque(nums)
p2_ans = len(stones)

while stones:
    stone_val, blink_itr = stones.popleft()
    p2_ans += itr(stone_val, blink_itr)

print(p1_ans)
print(p2_ans)









