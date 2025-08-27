'''
Best Time to Buy and Sell Stock
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
'''

# Time Complexity: O(N) where N is the length of prices due to iterating over all the prices once
# Space Complexity: O(1) due to uses constant extra space
def maxProfit(prices: list[int]) -> int:
    maxprof = 0
    smallest = prices[0]
    for i in range(1, len(prices)):
        if prices[i] - smallest >= maxprof:
            maxprof = prices[i] - smallest
        smallest = min(smallest, prices[i])

    return maxprof

# Test Cases
assert maxProfit([10,1,5,6,7,1]) == 6
assert maxProfit([10,8,7,5,2]) == 0