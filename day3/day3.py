import pandas as pd
import numpy as np
import re

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        inp = file.read()

    # P1
    pattern = r"mul\((\d+),(\d+)\)"
    num_pairs = re.findall(pattern, inp)
    num_pairs = [(int(pair[0]), int(pair[1])) for pair in num_pairs]
    p1_ans = sum([pair[0] * pair[1] for pair in num_pairs])
    print(p1_ans)

    # P2
    def find_mul_pairs_ans(data: str) -> int:
        """
        Given a string, find the mul(x,y) pattern pairs, and calculate the sum of the product of each pair
        :param data: string text
        :return: answer
        """

        pattern = r"mul\((\d+),(\d+)\)"
        num_pairs = re.findall(pattern, data)
        if len(num_pairs) == 0:
            return 0
        num_pairs = [(int(pair[0]), int(pair[1])) for pair in num_pairs]
        ans = sum([pair[0] * pair[1] for pair in num_pairs])
        return ans

    p2_ans = 0
    # Split on all the "don't()" strings
    dont_split = inp.split("don't()")
    # First entry here is before the first "don't()", which by default enables us to do any multiplications in there
    first_chain, dont_split = dont_split[0], dont_split[1:]

    if len(first_chain) != 0:
        # Add the answer from the first entry
        p2_ans += find_mul_pairs_ans(first_chain)

    # Note that an entry here is a string that is in between two "don't()" strings
    for entry in dont_split:
        if len(entry) == 0:
            # empty string
            continue

        # Split on "do()"
        do_split = entry.split("do()")

        # Ensure that the length is bigger than 1. Reason for that is that the first entry in this list should be
        # a sequence of strings that follows a "don't()", so we will not apply the multiplication. Anything after that
        # in list of string sequences are between two "do()" strings, and thus should be used in calculating the ans
        if len(do_split) > 1:
            do_split = do_split[1:]
            for entry in do_split:
                p2_ans += find_mul_pairs_ans(entry)

    print(p2_ans)





