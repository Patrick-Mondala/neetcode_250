'''
Find the Town Judge
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Constraints:

1 <= n <= 1000
0 <= trust.length <= 10,000
trust[i].length == 2
All the pairs of trust are unique.
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= n
'''

def findJudge(n: int, trust: list[list[int]]) -> int:
    """
    Implement findJudge
    """

# Test Cases
n = 4
trust = [[1,3],[4,3],[2,3]]
assert findJudge(n, trust) == 3

n = 3
trust = [[1,3],[2,3],[3,1],[3,2]]
assert findJudge(n, trust) == -1