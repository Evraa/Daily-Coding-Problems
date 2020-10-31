class LRUCache:

    def __init__(self, capacity: int):
        self.mapy = {}
        # self.last_used_key = None
        self.cap = capacity
        self.lru_last = []
        self.size = 0
        
    def update_last(self, key):
        # print (self.lru_last)
        if key in self.lru_last:
            self.lru_last.remove(key)
            self.lru_last.append(key)
        else:
            self.lru_last.append(key)
        return
    
    def get(self, key: int) -> int:

        if key in self.mapy.keys():
            self.update_last(key)
            return self.mapy[key]
        return -1

    
    def put(self, key: int, value: int) -> None:
        #exceeds limit??
        if self.cap == 0:
            return
        
        # if self.size < self.cap:
        if len(self.mapy) < self.cap:
            # self.size += 1
            self.mapy[key] = value
            self.update_last(key)
            
        else:
            if key in self.mapy.keys():
                self.mapy[key] = value
                self.update_last(key)
                return
            
            key_removed = self.lru_last[0]
            del self.mapy[key_removed]
            del self.lru_last[0]
            self.mapy[key] = value
            self.update_last(key)
            
    
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)