'''
Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same day. Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

Find and return the maximum profit you can achieve.

Constraints:

1 <= prices.length <= 30,000
0 <= prices[i] <= 10,000
'''

def maxProfit(prices: list[int]) -> int:
    """
    Implement maxProfit
    """

# Test Cases
prices = [7,1,5,3,6,4]
assert maxProfit(prices) == 7

prices = [1,2,3,4,5]
assert maxProfit(prices) == 4