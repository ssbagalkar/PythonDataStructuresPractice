# https://leetcode.com/problems/maximum-profit-in-job-scheduling
# this is not a good solution. It runs in quadratic time and time outs

# Passes 22/27 cases on leetcode. Try to find more optimal solution

from typing import List
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    scheduling_list = sorted([(startTime[ii], endTime[ii], profit[ii]) for ii in range(n)], key=lambda x: x[1])
    profit = [x[2] for x in scheduling_list]
    startTime = [x[0] for x in scheduling_list]
    endTime = [x[1] for x in scheduling_list]
    total_profits = [x for x in profit]
    for ii in range(1, n):
        for jj in range(ii):
            if startTime[ii] >= endTime[jj]:
                total_profits[ii] = max(total_profits[ii], profit[ii] + total_profits[jj])
    return max(total_profits)
