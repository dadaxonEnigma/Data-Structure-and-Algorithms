# stock_prices = []
# with open("stock_prices.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices.append([day,price])
# stock_prices
# [['march 6', 310.0],
#  ['march 7', 340.0],
#  ['march 8', 380.0],
#  ['march 9', 302.0],
#  ['march 10', 297.0],
#  ['march 11', 323.0]]
# stock_prices[0]

class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None        
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t.arr