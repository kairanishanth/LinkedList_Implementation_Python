class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    def printLL(self):
            if self.head is None:
                print("ll is empty")
            else:
                temp=self.head
                while temp is not None:
                    print(temp.data)
                    temp=temp.next
                
LL=Linkedlist()
LL.add_end(30)
LL.add_end(50)
LL.printLL()
        
