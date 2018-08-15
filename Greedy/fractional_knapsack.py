## Reference code - https://www.sanfoundry.com/python-program-solve-fractional-knapsack-problem-using-greedy-algorithm/
## Reference video-https://www.youtube.com/watch?v=oTTzNMHM05I
"""Return maximum value of items and their fractional amounts.

    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.

    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.

    capacity is the maximum weight.
    """


def fractional_knapsack(value, weight, capacity):
	# index = [0, 1, 2, ..., n - 1] for n items
	index = list(range(len(value)))
	# contains ratios of values to weight
	ratio = [v / w for v, w in zip(value, weight)]
	# index is sorted according to value-to-weight ratio in decreasing order
	index.sort(key=lambda x: ratio[x], reverse=True)
	
	max_value = 0
	fractions = [0] * len(value)
	for ii in index:
		if capacity > weight[ii]:
			capacity -= weight[ii]
			max_value += value[ii]
			fractions[ii] = 1
		else:
			max_value += capacity/weight[ii] * value[ii]
			fractions[ii] = capacity/weight[ii]
			capacity=0
			break
	
	return (max_value, fractions)


value = [3, 5, 1, 2, 4]
weight = [40, 50, 20, 10, 30]
capacity = 50
print(fractional_knapsack(value, weight, capacity))