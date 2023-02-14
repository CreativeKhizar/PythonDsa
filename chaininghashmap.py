class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class HashNode:
    def __init__(self,val=0,down=None,right=None):
        self.val=val
        self.down=down
        self.right=right


class ChainHash:
    def __init__(self):
        self.MAX=10
        self.head=HashNode()
        i=1
        temp=self.head
        while(i<=9):
            temp2=HashNode()
            temp.down=temp2
            temp=temp2
            i=i+1

    def gethash(self,val):
        h=val%self.MAX
        return h

    def insert(self,val):
        h=self.gethash(val)
        temp=self.head
        i=0
        while i<h:
            temp=temp.down
            i=i+1
        if temp.val==0:
            temp.val=val
        else:
            if temp.right==None:
                temp.right=Node(val)
            else:
                temp2=temp.right
                while(temp2.next!=None):
                    temp2=temp2.next
                temp2.next=Node(val)

    def delete(self,val):
        h=self.gethash(val)
        i=0
        temp=self.head
        while i<h:
            temp=temp.down
            i=i+1
        if temp.val==val:
            if temp.right==None:
                temp.val=0
            else:
                temp.val=temp.right.val
                temp.right=temp.right.next
        else:
            t=temp.right
            c=temp
            while(t!=None and t.val!=val):
                c=t
                t=t.next
            if(t!=None):
                c.next=t.next
            else:
                print("The Element doesnot exist")
        

    def search(self,val):
        h=self.gethash(val)
        i=0
        temp=self.head
        while i<h:
            temp=temp.down
            i=i+1
        j=0
        if(temp.val==val):
            print("Position ",i,",",j)
        else:
            j=1
            temp2=temp.right
            while(temp2!=None and temp2.val!=val):
                temp2=temp2.next
                j=j+1
            if(temp2!=None):
                print("Position ",i,",",j)
            else:
                print("Element doesnot exist")
        
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="")
            temp2=temp.right
            while(temp2!=None):
                print("->",temp2.val,end=" ")
                temp2=temp2.next
            print("->None")
            temp=temp.down

h=ChainHash()

while True:
    print("Enter your choice 1.Insert 2.Delete 3.Search 4.Display 5.Exit")
    ch=int(input())
    if ch==1:
        print("Enter the value to insert ")
        val=int(input())
        h.insert(val)

    elif ch==2:
        print("Enter the value to delete ")
        val=int(input())
        h.delete(val)

    elif ch==3:
        print("Enter the value to search ")
        val=int(input())
        h.search(val)

    elif ch==4:
        h.display()

    elif ch==5:
        break

    else:
        print("Invalid choice")


