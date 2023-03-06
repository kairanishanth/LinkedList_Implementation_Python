## remove the nth node from the end of the linkedlist:
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class LinkedList:
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
    def printll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
    def del_nth_node(self,head,n):
        slow=fast=head 
        for i in range(n):
            fast=fast.next 
        if fast is None:
            return head.next 
        while fast.next is not None:
            fast=fast.next 
            slow=slow.next  
        slow.next=slow.next.next 
obj1=LinkedList()
obj1.add_end(20)
obj1.add_end(30)
obj1.add_end(40)
obj1.add_end(50)
obj1.add_end(60)
obj1.del_nth_node(obj1.head,2)
obj1.printll()