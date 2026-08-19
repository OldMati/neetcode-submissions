class MyHashMap:

    def __init__(self):
        self.hashmap = [(None,)] * 16 # Storing tuples (int, int); key is None for not used, -1 for removed 
        self.size = 0
        self.capacity = 16

    def put(self, key: int, value: int) -> None:
        self.size += 1
        if self.size >= 0.75 * self.capacity:
            self._resize()

        hash_key = key % self.capacity

        while self.hashmap[hash_key][0] not in (-1, None, key):
            hash_key = (hash_key + 1) % self.capacity
        
        self.hashmap[hash_key] = (key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.capacity

        while self.hashmap[hash_key][0] not in (None, key):
            hash_key = (hash_key + 1) % self.capacity
        
        res = self.hashmap[hash_key]
        return -1 if res[0] in (-1, None) else res[1] # if remover or not inserted, remove -1 else value

    def remove(self, key: int) -> None:
        hash_key = key % self.capacity

        while self.hashmap[hash_key][0] not in (None, key):
            hash_key = (hash_key + 1) % self.capacity
        
        if self.hashmap[hash_key][0] == key:
            self.hashmap[hash_key] = (-1,)

    def _resize(self):
        self.capacity *= 2
        new_map = [(None,)] * self.capacity

        for tup in self.hashmap:
            if tup[0] not in (-1, None):
                key, val = tup
                self.put(key, val)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)