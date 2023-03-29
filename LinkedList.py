class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def insert_at_start(self,newdata):
      newNode=Node(newdata)
      newNode.nextval=self.headval
      self.headval=newNode
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode
   def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return
   def delete_at_start(self):
      if self.headval is None:
         print('empty list')
         return
      self.headval=self.headval.nextval

   def delete_at_end(self):
      if self.headval is None:
         print('no element')
         return
      n=self.headval
      while n.nextval.nextval is not None:
         n=n.nextval
      n.nextval=None
   def search(selx,x):
      if self.headval is None:
         print('empty')
         return
      n=self.headval
      while n is not None:
         if n.dataval==x:
            print('item found')
            return True
         n=n.nextval
      print('not found')
      return False
   def get_count(self):
      count=0
      n=self.headval
      while n.nextval is not None:
         n=n.nextval
         count+=1
      return count
   def insert_at_index(self,index,data):
      if index==1:
         new_node=Node(data)
         new_node.nextval=self.headval
         self.s=headval=new_node
      i=1
      n=self.headval
      while i<index-1 and n is not None:
         n=n.nextval
         i=i+1
      if n is None:
         print('out of found')
      else:
         new_node=Node(data)
         new_node.nextval=n.nextval
         n.nextval=new_node
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2

e2.nextval = e3
list.insert_at_start('Sun')
list.delete_at_end()
list.AtEnd("Thu")
list.insert_at_index(1,555)
list.listprint()

print(list.get_count())