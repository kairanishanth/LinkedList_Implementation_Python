#deleting the node at begin:
#inserting at specific position:
from ast import Delete


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
    def delete_begin(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            self.head=self.head.next
   
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
            
obj1=LinkedList()
obj1.add_begin(10)
obj1.add_begin(20)
obj1.delete_begin()
obj1.delete_begin()
obj1.print_ll()
