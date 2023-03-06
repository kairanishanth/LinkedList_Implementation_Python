#LINKED LIST : 
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None 
#creating the Linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
#traversing the linked list
    def print_ll(self):
        if self.head is None:
            print("linkedlist is empty ")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
#adding the elements:
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    
        
obj1=LinkedList()
obj1.insert_begin(20)
obj1.insert_end(30)
obj1.insert_end(40)
obj1.insert_begin(10)
obj1.print_ll()
