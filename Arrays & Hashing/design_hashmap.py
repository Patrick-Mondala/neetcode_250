'''
Design HashMap
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Constraints:

0 <= key, value <= 1,000,000
At most 10,000 calls will be made to put, get, and remove.
'''

# Time Complexity: O(1) for put, get, and remove operations
# Space Complexity: O(N) where N is the range of possible keys (1,000,001)
class MyHashMap:

    def __init__(self):
        self.arr = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1

# Test Cases
hashMap = MyHashMap()
hashMap.put(1, 1)      # The map is now [[1,1]]
hashMap.put(2, 2)      # The map is now [[1,1], [2,2]]
assert hashMap.get(1) == 1 # return 1, The map is now [[1,1], [2,2]]
assert hashMap.get(3) == -1 # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
hashMap.put(2, 1)      # The map is now [[1,1], [2,1]] (i.e., update the existing value)
assert hashMap.get(2) == 1 # return 1, The map is now [[1,1], [2,1]]
hashMap.remove(2)      # remove the mapping for 2, The map is now [[1,1]]
assert hashMap.get(2) == -1 # return -1 (i.e., not found), The map is now [[1,1]]