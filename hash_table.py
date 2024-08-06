# class HashTable:
#     def __init__(self) -> None:
#         self.MAX = 10
#         self.arr = [[] for i in range(self.MAX)]
    
#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
    
#     def __setitem__(self,key,val):
#        h = self.get_hash(key)
#        found = False
#        for idx, element in enumerate(self.arr[h]):
#            if len(element) == 2 and element[0] == key:
#                self.arr[h][idx] = (key,val)
#                found = True
#                break
#        if not found:
#            self.arr[h].append((key,val))
            
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
    
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         for index, element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 del self.arr[h][index]
        
    
# t = HashTable()
# t['march 6'] = 100
# t['march 19'] = 430
# t['march 31'] = 3000
# t['march 17'] = 0
# print(t['march 17'])
# del t['march 17']
# print(t.arr)

# list = [[], [('march 19', 430)], [], [], [], [('march 31', 3000)], [], [], [], [('march 6', 100), ('march 17', 0)]]
# for element in list[9]:
#     print(element[0])
