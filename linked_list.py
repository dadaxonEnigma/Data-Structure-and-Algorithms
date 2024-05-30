# class Node:
#     def __init__(self, data=None,next=None):
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
#     def insert_at_begining(self,data):
#         node = Node(data,self.head)
#         self.head = node
#     def print(self):
#         if self.head is None:
#             print("Linked lis ist empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + '-->'
#             itr = itr.next
#         print(llstr)
    
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data,None)
#             return

#         itr = self.head
#         while itr.next:
#             itr = itr.next
        
#         itr.next = Node(data, None)

# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_at_end(79)
#     ll.insert_at_end(1)
#     ll.insert_at_end(349)
#     ll.insert_at_begining(3)
    
#     ll.print()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"[{self.data}]->{self.next}"

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __str__(self) -> str:
        return str(self.head)

if __name__ == '__main__':
    linked_list = LinkedList()
    temp = Node(1)
    linked_list.head = temp
    for i in range(2,9):
        temp.next  = Node(i)
        temp = temp.next
    print(linked_list)