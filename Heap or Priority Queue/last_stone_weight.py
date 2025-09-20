'''
Last Stone Weight
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Constraints:

1 <= stones.length <= 20
1 <= stones[i] <= 100
'''

def lastStoneWeight(stones: list[int]) -> int:
    """
    Implement lastStoneWeight
    """

# Test Cases
stones = [2,3,6,2,4]
assert lastStoneWeight(stones) == 1

stones = [1,2]
assert lastStoneWeight(stones) == 1