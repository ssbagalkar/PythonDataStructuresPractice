# explanation - https://medium.com/outco/how-to-solve-the-house-robber-problem-f3535ebaef1b
# leetcode - https://leetcode.com/problems/house-robber/
# https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
# https://upcount.tistory.com/87
## Best explanation https://www.youtube.com/watch?v=xlvhyfcoQa4

def rob(houses):
    if len(houses) == 0:
        return 0
    if len(houses) == 1:
        return houses[0]
    if len(houses) == 2:
        return max(houses[0], houses[1])
    else:
        dp = {}
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for ii in range(2, len(houses)):
            dp[ii] = max(houses[ii] + dp[ii-2], dp[ii-1])
        return dp[len(houses)-1]








# arr = [2, 9, 4, 5, 6]
# arr = [3, 10, 3, 1, 2]
arr = [2, 1, 1, 2]
print(rob(arr))