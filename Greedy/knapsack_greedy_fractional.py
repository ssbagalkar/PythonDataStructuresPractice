
#https://www.youtube.com/watch?v=oTTzNMHM05I&t=623s
def knapsack_fractional_greedy(profits, weights, max_permissible_weight):
    remaining_weight = max_permissible_weight
    total_profit = 0
    profit_by_weight = [x/y for (x, y) in zip(profits,weights)]
    while len(profit_by_weight) > 0 and remaining_weight > 0:
        max_index = profit_by_weight.index(max(profit_by_weight))
        current_weight = weights.pop(max_index)
        if current_weight < remaining_weight:
            total_profit += profits.pop(max_index)
            remaining_weight -= current_weight
        else:
            total_profit += remaining_weight/current_weight * profits.pop(max_index)
            remaining_weight -= remaining_weight
        profit_by_weight.pop(max_index)
    return total_profit

profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]

print(knapsack_fractional_greedy(profits, weights, max_permissible_weight=15))
