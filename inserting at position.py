#inserting at specific position:
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None 
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_position(self,data,position):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            count=1 
            while temp is not None and count<position:
                temp=temp.next
                count+=1 
            new_node.next=temp.next
            temp.next=new_node
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
obj1=LinkedList()
obj1.add_begin(30)
obj1.add_begin(40)
obj1.insert_at_position(20,30)
obj1.print_ll()
