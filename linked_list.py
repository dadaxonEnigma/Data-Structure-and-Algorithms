class Node:
    def __init__(self,data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(data,None)
    
    def print_list(self):
        if self.head is None:
            print('Linked List is empty')
            return
        cur_node = self.head
        llstr = ''
        while cur_node:
            llstr += str(cur_node.data) + '-->'
            cur_node = cur_node.next
        print(llstr)
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index>=self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        cur_node = self.head
        while cur_node:
            if count == index - 1:
                cur_node.next = cur_node.next.next
                break
            cur_node = cur_node.next
            count += 1
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


llist = LinkedList()
llist.insert_at_start('1')
llist.insert_at_start('2')
llist.insert_at_end('5')
llist.insert_values([2,4,5,5,6,6,6])
llist.remove_at(1)
print(llist.get_length())
llist.print_list()
