class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_begin(self,data):
        new_node = Node(data) 
        new_node.next = self.head 
        self.head =  new_node 
    
    def insert_end(self,data):
        new_node = Node(data) 
        if self.head is None:
            self.head=new_node 
        else:
            temp=self.head 
            while temp.next is not None:
                temp=temp.next 
            temp.next = new_node  
    
    def insertAfterXdata(self,x,data):
        new_node = Node(data)
        curr_node =self.head 
        while curr_node is not None:
            if curr_node.data == x:
                new_node.next = curr_node.next
                curr_node.next =new_node 
                return 
            curr_node=curr_node.next 
    
    def Traversing(self):
        if self.head is None:
            print("Linkedist  is Empty")
        else:
            temp=self.head
            while temp is  not None:
                print(temp.data)
                temp=temp.next

obj1 = LinkedList()
obj1.insert_begin(40) 
obj1.insert_begin(30)     
obj1.insert_begin(20)
obj1.insert_begin(10)  
obj1.insert_end(50)           
obj1.insert_end(60)
obj1.insertAfterXdata(30,100)
obj1.Traversing()       