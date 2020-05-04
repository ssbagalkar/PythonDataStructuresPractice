## O(n)- time
## Reference video - https://www.youtube.com/watch?v=blUwDD6JYaE&t=49s

## This is the simplest solution so far

def max_profit(prices):
	n = len(prices)
	profit = 0
	if n < 2:
		return profit
	for ii in range(n - 1):
		if prices[ii + 1] - prices[ii] > 0:
			profit += prices[ii + 1] - prices[ii]
	return profit


prices = [7, 1, 5, 13, 16, 4]
print(max_profit(prices))
