#http://www.techiedelight.com/coin-change-problem-find-total-number-ways-get-denomination-coins/

def coinChange(coinList, numOfCoins, amount):
    # if total is 0, return 1
    if (amount == 0):
        return 1

    # return 0 if total become negative or no elements are left
    if (amount < 0 or numOfCoins < 0):
        return 0

    include = coinChange(coinList,numOfCoins,amount-coinList[numOfCoins])
    exclude = coinChange(coinList,numOfCoins-1,amount)

    return include + exclude



coinList = [1, 2, 3]
numOfCoins = len(coinList)
amount = 4
print(coinChange(coinList, numOfCoins-1, amount))