class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class LinkedList: #creating the linkedlist
    def __init__(self):
        self.head=None
    def add_begin(self,data):#adding the element at begin in the linked list\
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def PrintLL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
         
   
LL=LinkedList()
LL.add_begin(20)
LL.PrintLL()
        
