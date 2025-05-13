"""
I implemented a hash set using an array of lists to handle collisions through chaining. In the add method, I calculate the hash and insert the key into the corresponding list if it's not already there. For remove and contains, I use the same hash to find the correct list and check or delete the key.
"""
class MyHashSet:

    def __init__(self):
        self.size = 10 ** 4
        self.hash_table = [None] * self.size

    def calculate_hash_value(self, key: int) -> int:
        return key % self.size
        
    def add(self, key: int) -> None:
        hash_value = self.calculate_hash_value(key)
        if self.hash_table[hash_value] == None:
            self.hash_table[hash_value] = [key]
        else:
            self.hash_table[hash_value].append(key)
        
    def remove(self, key: int) -> None:
        hash_value = self.calculate_hash_value(key)
        if self.hash_table[hash_value] != None:
            while key in self.hash_table[hash_value]:
                self.hash_table[hash_value].remove(key)

    def contains(self, key: int) -> bool:
        hash_value = self.calculate_hash_value(key)
        if self.hash_table[hash_value] == None:
            return False
        else:
            return key in self.hash_table[hash_value]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)