class TimeMap:

    def __init__(self):
        self.table = {} # key -> list[(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table or len(self.table[key]) == 0:
            return ''

        arr = self.table[key]
        # find the max timestamp_prev <= timestamp
        l = 0
        r = len(arr) - 1
        
        res = ""
        while l <= r:
            c = (l + r) // 2
            if arr[c][0] > timestamp:
                r = c - 1
            else:
                res = arr[c][1]
                l = c + 1
        
        return res
        
