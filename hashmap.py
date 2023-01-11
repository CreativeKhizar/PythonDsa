class HashTable:
    def __init__(self):
        self.MAX=15
        self.arr=[[] for i in range(self.MAX)]

    def gethash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    def setitem(self,key,val):
        h=self.gethash(key)
        for i in self.arr:
            if (key,value) in i:
                print("Inserted key, value already present")
                break
        self.arr[h].append((key,val))

    def getitem(self,key):
        h=self.gethash(key)
        return self.arr[h]

    def delitem(self,key,value):
        h=self.gethash(key)
        if len(self.arr[h])==1:
            self.arr[h]=[]
        else:
            for i in range(len(self.arr[h])):
                if self.arr[h][i]==(key,value):
                    self.arr[h].pop(i)
                    break

    def display(self):
        for i in self.arr:
            print(i,end="")
        print()
        
t=HashTable()

while True:
	ch=int(input("Enter your choice 1.Insert 2.Delete 3.Get value of key 4.Display 5.Exit"))
	
	if ch==1:
		print("Enter the key and value")
		key=input()
		value=int(input())
		t.setitem(key,value)
	elif ch==2:
		print("Enter the key and value to delete")
		key=input()
		value=int(input())
		t. delitem(key,value)
	elif ch==3:
		print("Enter key to know its value")
		key=input()
		print(t.getitem(key))
	elif ch==4:
		t.display()
	elif ch==5:
		break
	else:
	 	print("Invalid choice")
		
		
