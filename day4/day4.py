import pandas as pd
import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        txt = file.read()
        rows = txt.split("\n")

    num_r = len(rows)
    num_c = len(rows[0])

    # P1
    p1_ans = 0

    for r in range(num_r):
        for c in range(num_c):
            # right
            if c+3 < num_c and rows[r][c] == "X" and rows[r][c+1] == "M" and rows[r][c+2] == "A" and rows[r][c+3] == "S":
                p1_ans += 1

            # left
            if c-3 >= 0 and rows[r][c] == "X" and rows[r][c-1] == "M" and rows[r][c-2] == "A" and rows[r][c-3] == "S":
                p1_ans += 1

            # down
            if r+3 < num_r and rows[r][c] == "X" and rows[r+1][c] == "M" and rows[r+2][c] == "A" and rows[r+3][c] == "S":
                p1_ans +=1

            # up
            if r-3 >= 0 and rows[r][c] == "X" and rows[r-1][c] == "M" and rows[r-2][c] == "A" and rows[r-3][c] == "S":
                p1_ans += 1

            # diag (up, right)
            if r-3 >= 0 and c+3 < num_c and rows[r][c] == "X" and rows[r-1][c+1] == "M" and rows[r-2][c+2] == "A" and rows[r-3][c+3] == "S":
                p1_ans +=1

            # diag (up, left)
            if r-3 >= 0 and c-3 >= 0 and rows[r][c] == "X" and rows[r-1][c-1] == "M" and rows[r-2][c-2] == "A" and rows[r-3][c-3] == "S":
                p1_ans +=1

            # diag (down, right)
            if r+3 < num_r and c+3 < num_c and rows[r][c] == "X" and rows[r+1][c+1] == "M" and rows[r+2][c+2] == "A" and rows[r+3][c+3] == "S":
                p1_ans +=1

            # diag (down, left)
            if r+3 < num_r and c-3 >= 0 and rows[r][c] == "X" and rows[r+1][c-1] == "M" and rows[r+2][c-2] == "A" and rows[r+3][c-3] == "S":
                p1_ans +=1

    print(p1_ans)

    # P2
    p2_ans = 0
    for r in range(num_r):
        for c in range(num_c):
            if rows[r][c] == "A":
                if r-1 >= 0 and r+1 < num_r and c-1 >= 0 and c+1 < num_c:
                    # We have 4 options:

                    # M   M
                    #   A
                    # S   S
                    if rows[r-1][c-1] == "M" and rows[r-1][c+1] == "M" and rows[r+1][c-1] == "S" and rows[r+1][c+1] == "S":
                        p2_ans += 1

                    # S   M
                    #   A
                    # S   M
                    if rows[r-1][c-1] == "S" and rows[r-1][c+1] == "M" and rows[r+1][c-1] == "S" and rows[r+1][c+1] == "M":
                        p2_ans += 1

                    # M   S
                    #   A
                    # M   S
                    if rows[r-1][c-1] == "M" and rows[r-1][c+1] == "S" and rows[r+1][c-1] == "M" and rows[r+1][c+1] == "S":
                        p2_ans += 1

                    # S   S
                    #   A
                    # M   M
                    if rows[r-1][c-1] == "S" and rows[r-1][c+1] == "S" and rows[r+1][c-1] == "M" and rows[r+1][c+1] == "M":
                        p2_ans += 1

    print(p2_ans)




