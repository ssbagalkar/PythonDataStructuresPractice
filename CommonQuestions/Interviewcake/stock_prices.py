#https://www.interviewcake.com/
import math

stock_prices = [10, 7, 5, 8, 11, 9]


def make_max_profit(stock_prices):
	max_profit = -math.inf
	current_min = stock_prices[0]
	for ii in range(1, len(stock_prices)):
		price = stock_prices[ii]
		current_profit = price - current_min
		if current_profit > max_profit:
			max_profit = current_profit
		if price < current_min:
			current_min = price
	
	return max_profit


print(make_max_profit(stock_prices))