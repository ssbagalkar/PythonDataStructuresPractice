# Question - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# this is simple brute force approach. o(n^2) complexity
def max_profit_buy_and_sell_stock_just_once(arr):
    max_profit = -1
    n = len(arr)
    for ii in range(n):
        for jj in range(ii, n):
            if arr[jj] - arr[ii] > max_profit:
                max_profit = arr[jj] - arr[ii]
    return max_profit

# this is better solution. time complexity is o(n)

# Verified solution on leetcode. Runs 94.7% (runtime)faster tha other submissions
def max_profit_buy_and_sell_stock_just_once_efficient(arr):
    n = len(arr)
    if n < 2:
        return 0
    local_min = arr[0]
    max_profit = 0

    for ii in range(1, n):
        if (arr[ii] - local_min) > max_profit:
            max_profit = arr[ii] - local_min
        if arr[ii] < local_min:
            local_min = arr[ii]
    return max_profit

# arr = [7, 1, 5, 3, 6, 4]
arr = [7, 6, 4, 3, 1]
print(max_profit_buy_and_sell_stock_just_once_efficient(arr))