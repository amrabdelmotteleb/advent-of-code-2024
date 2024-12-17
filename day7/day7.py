from itertools import product

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip()

equation_dict = {}
for line in data.split("\n"):
    res, equation = line.split(":")
    res = int(res)
    equation = [int(num) for num in equation.strip().split(" ")]
    equation_dict[res] = equation

p1_operators = ["+", "*"]

# P1
for val, equation in equation_dict.items():
    num_ops = len(equation) - 1
    # All possible permutations
    op_perms = list(product(p1_operators, repeat=num_ops))
    for op_perm in op_perms:
        cur_ans = equation[0]
        for op, num in zip(op_perm, equation[1:]):
            if op == "+":
                cur_ans += num
            elif op == "*":
                cur_ans *= num

        if cur_ans == val:
            p1_ans += val
            break


# P2
p2_operators = ["+", "*", "||"]
for val, equation in equation_dict.items():
    num_ops = len(equation) - 1
    # All possible permutations
    op_perms = list(product(p2_operators, repeat=num_ops))
    for op_perm in op_perms:
        cur_ans = equation[0]
        for op, num in zip(op_perm, equation[1:]):
            if op == "+":
                cur_ans += num
            elif op == "*":
                cur_ans *= num
            elif op == "||":
                cur_ans = int(str(cur_ans) + str(num))

        if cur_ans == val:
            p2_ans += val
            break

print(p1_ans)
print(p2_ans)

# A more efficient solution for both P1 and P2:
p1_ans2 = 0
p2_ans2 = 0
def check_validity(val: int, eq: list[int], p2: bool) -> bool:
    if len(eq) == 1:
        return val == eq[0]
    # Addition case
    if check_validity(val, [eq[0]+eq[1]] + eq[2:], p2):
        return True

    # Multiplication case
    if check_validity(val, [eq[0]*eq[1]] + eq[2:], p2):
        return True

    # Concatenation case
    if p2 and check_validity(val, [int(str(eq[0]) + str(eq[1]))] + eq[2:], p2):
        return True

    return False

for val, equation in equation_dict.items():
    # P1
    if check_validity(val, equation, p2=False):
        p1_ans2 += val

    if check_validity(val, equation, p2=True):
        p2_ans2 += val

print(p1_ans2)
print(p2_ans2)






