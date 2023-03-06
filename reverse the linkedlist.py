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
    
#reverse the linked list:
    def reversell(self):
        prev=None
        curr=self.head 
        while curr is not None:
            next=curr.next 
            curr.next=prev 
    # Updating or shifting the nodes
            prev=curr
            curr=next 
        self.head=prev
    def printll(self):
        if self.head is None:
            print("linked list is empty ")
        else:
            temp=self.head 
            while temp is not None:
                print(temp.data)
                temp=temp.next 
           
obj1=LinkedList()
obj1.add_begin(20)
obj1.add_begin(30)
obj1.add_begin(40)
obj1.add_begin(50)
obj1.reversell()
obj1.printll()

        