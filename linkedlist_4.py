#Insertion of Node in between two node of the linked list

class Node:
        def __init__(self,dataVal=None):
                self.dataval=dataVal
                self.nextval=None

        
class LinkedList:
        def __init__(self):
                self.headval=None

        def traverse(self):
                printval=S.headval
                while(printval!=None):
                        print(printval.dataval)
                        printval=printval.nextval


        def insertinBetween(self,new,data):
                NewNode=Node(new)
                currentnode=self.headval
                while(currentnode.dataval!=data):
                        #print(currentnode.dataval)
                        currentnode=currentnode.nextval
                NewNode.nextval=currentnode.nextval
                currentnode.nextval=NewNode
                
                        


S=LinkedList()
S.headval=Node(1)
q=Node(2)
r=Node(3)
S.headval.nextval=q
q.nextval=r
t=Node(5)
r.nextval=t
print("before insertion")
S.traverse()
S.insertinBetween(4,3)
print("After insertion ")
S.traverse()
