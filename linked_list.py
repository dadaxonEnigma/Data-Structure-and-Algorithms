# class Node:
#     def __init__(self,data = None, next = None) -> None:
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
    
    
#     def insert_at_start(self,data):
#         node = Node(data, self.head)
#         self.head = node
    
    
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         cur_node = self.head
#         while cur_node.next:
#             cur_node = cur_node.next
#         cur_node.next = Node(data, None)
    
#     def print_list(self):
#         if self.head is None:
#             print('Linked List is empty!')
#         cur_node = self.head
#         llstr = ''
#         while cur_node:
#             llstr += str(cur_node.data) + '--->'
#             cur_node = cur_node.next
#         print(llstr)
    
    
#     def get_length(self):
#         cur_node = self.head
#         count = 0
#         while cur_node:
#             count += 1
#             cur_node = cur_node.next
#         return count
    
    
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
            
    
#     def remove_at(self, index):
#         if index < 0 or index >= self.get_length():
#             raise Exception("Invalid index!")
#         if index == 0:
#             self.head = self.head.next
#             return
#         count = 0
#         cur_node = self.head
#         while cur_node:
#             if count == index - 1:
#                 cur_node.next = cur_node.next.next
#                 break
#             cur_node = cur_node.next
#             count += 1
    
    
#     def insert_at(self, index, data):
#         if index < 0 or index >= self.get_length():
#             raise Exception("invalid index!")
#         if index == 0:
#             self.insert_at_start(data)
#             return
#         count = 0
#         cur_node = self.head
#         while cur_node:
#             if count == index - 1:
#                 cur_node.next = Node(data,cur_node.next)
#                 break
#             cur_node = cur_node.next
#             count += 1
    
    
#     def insert_after_value(self,data_after, data_to_insert):
#         if self.head is None:
#             return
#         if self.head.data == data_after:
#             self.head.next = Node(data_to_insert,self.head.next)
#             return
#         cur_node = self.head
#         while cur_node:
#             if data_after == cur_node.data:
#                 cur_node.next = Node(data_to_insert,cur_node.next)
#             cur_node = cur_node.next

    
#     def remove_by_value(self,data):
#         if self.head is None:
#             return
                
#         cur_node = self.head
#         while cur_node.next:
#             if cur_node.next.data == data:
#                 cur_node.next = cur_node.next.next
#                 break
#             cur_node = cur_node.next
                
# ll = LinkedList()
# ll.insert_at_start(1)
# ll.insert_at_start(0)
# ll.insert_at_end(2)
# ll.insert_values([0,1,2])
# ll.insert_at(2,1.5)
# ll.insert_after_value(1,0.5)
# ll.print_list()
