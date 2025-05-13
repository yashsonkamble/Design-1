"""
I first created a hashset using a Python set in the __init__ function. 
Then, I implemented basic methods to add a key, remove a key, and 
check if a key exists in the hashset.
"""
class MyHashSet:

    def __init__(self):
        self.hashset = set()
        
    def add(self, key: int) -> None:
        self.hashset.add(key)
        
    def remove(self, key: int) -> None:
        self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)