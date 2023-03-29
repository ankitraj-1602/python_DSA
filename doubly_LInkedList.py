class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("empty")
    
    def InsertToEnd(self, data):
        
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
  
    
    
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")
    def inert_at_pos(self,data,position):
        temp=self.start_node
        count=1
        while temp is not None:
            if count==position-1:
                break
            count+=1
            temp=temp.next
        if position==1:
            self.InsertToEmptyList(data)
        elif temp is None:
            print("there are less element")
        elif temp.next is None:
            self.InsertToEnd(data)
        else:
            new_node=Node(value)
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            temp.next=new_node
    def delete_last(self):
        if(self.start_node != None):
            if(self.start_node.next == None):
                self.start_node = None
            else:
                temp = self.start_node
                while(temp.next.next != None):
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None
x=doublyLinkedList()
x.InsertToEmptyList(33)
x.inert_at_pos(45,2)
x.delete_last()
x.Display()