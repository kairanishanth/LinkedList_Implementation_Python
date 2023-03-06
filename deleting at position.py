#deleting at position:
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
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    def add_at_position(self,data,position):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node 
        else:
            temp=self.head
            count=1 
            while temp is not None and count<position:
                temp=temp.next
                count+=1 
            temp.next=new_node
            new_node.next=temp.next
    def print_ll(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp=self.head 
            while temp is not None:
                print(temp.data)
                temp=temp.next
obj1=LinkedList()
obj1.add_begin(20)
obj1.add_begin(30)
obj1.add_begin(50)
obj1.add_at_position(50,30)
obj1.print_ll()

        