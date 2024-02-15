class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.table = [0]*self.size

    def put(self, key: int, value: int) -> None:
        idx = key%(self.size)
        if self.table[idx] == 0:
            self.table[idx] = [[key,value]]
        else:
            keyFound = False
            for i, item in enumerate(self.table[idx]):
                if item[0] == key:
                    item[1] = value
                    keyFound = True
            if not keyFound:
                self.table[idx].append([key,value])

    def get(self, key: int) -> int:
        idx = key%self.size
        if self.table[idx] == 0:
            return -1
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        idx = key%self.size
        if self.table[idx] != 0:
            for pair in self.table[idx]:
                if pair[0] == key:
                    self.table[idx].remove(pair)
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
