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
import heapq


# Time Complexity: O(N * log(N)) where N is the size of stones, due to popping from and pushing to the heap twice N/2 times
# Space Complexity: O(N) where N is the size of stones, due to storing the stones in a heap
def lastStoneWeight(stones: list[int]) -> int:
    r_stones = [-stone for stone in stones]
    heapq.heapify(r_stones)

    while len(r_stones) > 1:
        heaviest_stone = -heapq.heappop(r_stones)
        next_heaviest_stone = -heapq.heappop(r_stones)
        if heaviest_stone == next_heaviest_stone:
            continue
        heapq.heappush(r_stones, -(heaviest_stone - next_heaviest_stone))

    return -r_stones.pop() if r_stones else 0

# Test Cases
stones = [2,3,6,2,4]
assert lastStoneWeight(stones) == 1

stones = [1,2]
assert lastStoneWeight(stones) == 1