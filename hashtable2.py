class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[0 for i in range(self.MAX)]

    def get_hash(self,value):
        h=value
        return h%self.MAX

    def setitem(self,val):
        h=self.get_hash(val)
        if self.arr[h]==0:
            self.arr[h]=val
        else:
            #   Applying Linear Probabing
            for i in range(1,self.MAX):
                if self.arr[(h+i)%self.MAX]==0:
                       self.arr[(h+i)%self.MAX]=val
                       break
            else:
                print("Hash Table is full")

    def search(self,val):
        for i in range(self.MAX):
            if self.arr[i]==val:
                return i
        else:
            print(val," is not in Hash Table")
	    return -1


    def delitem(self,val):
        h=self.get_hash(val)
        if self.arr[h]==val:
            self.arr[h]=0
        else:
            for i in range(1,self.MAX):
                if self.arr[(h+i)%self.MAX]==val:
                       self.arr[(h+i)%self.MAX]=0
                       break

    def display(self):
        print(self.arr)


t=HashTable()

while True:
    ch=int(input("Enter your choice 1.Insert 2.Delete 3.Search 4.Display 5.Exit"))
	
    if ch==1:
        print("Enter the value to insert")
        value=int(input())
        t.setitem(value)
    elif ch==2:
        print("Enter the value to delete")
        value=int(input())
        t.delitem(value)
    elif ch==3:
        print("Enter the value to find its index")
        value=int(input())
        index=t.search(value)
        print(index)
    elif ch==4:
        t.display()
    elif ch==5:
        break
    else:
        print("Invalid choice")



    
