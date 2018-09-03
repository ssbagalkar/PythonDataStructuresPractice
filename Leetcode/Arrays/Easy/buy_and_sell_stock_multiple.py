## Write this code on my own
## Wirks perfectly
## O(n)- time
## Reference video - https://www.youtube.com/watch?time_continue=239&v=JaosdXkUWTs

def max_profit(stock_prices):
	local_maxima_found = False
	local_minima_found = False
	maximum_profit = 0
	for ii in range(len(stock_prices) - 1):
		
		if not local_minima_found:
			if stock_prices[ii + 1] >= stock_prices[ii]:
				local_minima_found = True
				local_minima = stock_prices[ii]
		
		if local_minima_found:
			if stock_prices[ii] >= stock_prices[ii + 1]:
				local_maxima_found = True
				local_maxima = stock_prices[ii]
		
		if local_maxima_found and local_minima_found:
			maximum_profit += local_maxima - local_minima
			local_maxima_found = False
			local_minima_found = False
			local_minima = None
			local_maxima = None
		
		if local_minima_found and ii==len(stock_prices)-2:
			if stock_prices[ii]<=stock_prices[ii+1]:
				local_maxima = stock_prices[ii+1]
				maximum_profit+=local_maxima-local_minima
	return maximum_profit


stock_prices = [1,9,6,9,1,7,1,1,5,9,9,9]
print(max_profit(stock_prices))