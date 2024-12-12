import pandas as pd
import numpy as np

reports = []

if __name__ == "__main__":
    with open("input.txt", "r") as lines:
        for line in lines:
            cur_lvl = np.array([int(l) for l in line.split()])
            reports.append(cur_lvl)

    # Part 1
    reports_diffs = [np.diff(cur_lvls) for cur_lvls in reports]
    ans_p1 = 0
    i = 0

    for report_diffs in reports_diffs:
        cond1 = (np.all(report_diffs > 0) | np.all(report_diffs < 0))
        cond2 = (np.all(abs(report_diffs) >= 1) & np.all(abs(report_diffs) <= 3))
        if cond1 and cond2:
            ans_p1+=1
            print(f"Index: {i}")
            print(f"Report: {reports[i]}")
            print(f"Report diff: {report_diffs}")
        i+=1

    # Part 2
    def check_conds(report: np.array) -> int:
        diffs = np.diff(report)
        cond1 = (np.all(diffs > 0) | np.all(diffs < 0))
        cond2 = (np.all(abs(diffs) >= 1) & np.all(abs(diffs) <= 3))
        if cond1 and cond2:
            return 1
        return 0

    ans_p2 = 0
    for report in reports:
        # Check first if it works fine without doing any changes
        success = check_conds(report)
        if success == 1:
            ans_p2 += 1

        else:
            for ind in range(len(report)):
                cur = np.delete(report, ind)
                success = check_conds(cur)
                if success == 1:
                    ans_p2 += 1
                    break
                    







