'''
Guess Number Higher Or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

0: your guess is equal to the number I picked (i.e. num == pick).
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
Return the number that I picked.

Constraints:

1 <= pick <= n <= ((2^31)-1)
'''

pick = None
def guess(num: int) -> int:
    if num == pick:
        return 0
    if num < pick:
        return 1
    if num > pick:
        return -1

# Time Complexity: O(logN) where N is the size of N
# Space Complexity: O(1) due to using constant extra space
def guessNumber(n: int) -> int:
    l, r = 0, n

    while True:
        mid = l + ((r - l) // 2)
        res = guess(mid)
        if res == 0:
            return mid
        if res == 1:
            l = mid + 1
        else:
            r = mid - 1

# Test Cases
pick = 3
assert guessNumber(5) == 3

pick = 10
assert guessNumber(15) == 10

pick = 1
assert guessNumber(1) == 1