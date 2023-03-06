class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def PrintLL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
                
    def add_begin(self,data):
        new_node=Node(data)
        new_node.temp=self.head
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
LL=Linkedlist()
LL.add_begin(10)
LL.add_end(30)
LL.PrintLL()
    
