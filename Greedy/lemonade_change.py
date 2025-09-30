'''
Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

You are given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Constraints:

1 <= bills.length <= 100,000
bills[i] is either 5, 10, or 20.
'''

# Time Complexity: O(N) where N is the length of bills due to iterating over every bill we receive
# Space Complexity: O(1) due to using constant extra space
def lemonadeChange(bills: list[int]) -> bool:
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        if bill == 10:
            tens += 1
            fives -= 1
        if bill == 20:
            if tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
        
        if fives < 0 or tens < 0:
            return False
    
    return True

# Test Cases
bills = [5,10,5,5,20]
assert lemonadeChange(bills) == True

bills = [5,20,10,5]
assert lemonadeChange(bills) == False