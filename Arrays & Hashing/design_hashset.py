'''
Design Hashset
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Constraints:

0 <= key <= 1,000,000
At most 10,000 calls will be made to add, remove, and contains.
'''

# Time Complexity: O(1) for add, remove, and contains operations
# Space Complexity: O(N) where N is the range of possible keys (1,000,001)
class MyHashSet:

    def __init__(self):
        self.arr = [False] * 1000001

    def add(self, key: int) -> None:
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        return self.arr[key]

# Test Cases
hashSet = MyHashSet()
hashSet.add(1)      # set = [1]
hashSet.add(2)      # set = [1, 2]
assert hashSet.contains(1) == True  # return True
assert hashSet.contains(3) == False # return False, (not found)
hashSet.add(2)      # set = [1, 2]
assert hashSet.contains(2) == True  # return True
hashSet.remove(2)   # set = [1]
assert hashSet.contains(2) == False # return False, (already removed)
