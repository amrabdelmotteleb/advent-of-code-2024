import pandas as pd
import numpy as np
import sys
from collections import Counter

l1 = []
l2 = []

if __name__ == "__main__":
    # Read data
    with open("input.txt", "r") as lines:
        for line in lines:
            L, R = line.split()
            L, R = int(L), int(R)
            l1.append(L)
            l2.append(R)

    # Q1
    l1_sorted_arr, l2_sorted_arr = np.array(sorted(l1)), np.array(sorted(l2))
    q1_ans = abs(l1_sorted_arr - l2_sorted_arr).sum()
    print(f"Q1's answer is: {q1_ans}")

    # Q2
    common_nums = set(l1).intersection(set(l2))
    counts = dict(Counter(l2_sorted_arr))
    relev_counts = {num: count for num, count in counts.items() if num in common_nums}
    mult_vals = [num*count for num, count in relev_counts.items()]
    q2_ans = sum(mult_vals)
    print(f"Q2's answer is: {q2_ans}")




