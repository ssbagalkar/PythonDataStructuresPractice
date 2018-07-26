# Naive greedy approach
# Find the minimum number of coins to use for a given amount using
# the denominatiosn given
def min_coin_change(denominations,amount):
	result_set=[]
	for ii in range(len(denominations)-1,-1,-1):
		while(amount>=denominations[ii]):
			amount-=denominations[ii]
			result_set.append(denominations[ii])
			
	return result_set
	

denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 76
print(min_coin_change(denominations,amount))
