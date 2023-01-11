class HashTable:
    def __init__(self):
        self.MAX=15
        self.arr=[[] for i in range(self.MAX)]

    def __get_hash__(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h=self.__get_hash__(key)
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
               self.arr[h][idx]=(key,val)
               found=True
               break
        if not found:
               self.arr[h].append((key,val))

    def __getitem__(self,key):
        h=self.__get_hash__(key)
        return self.arr[h]

    def __delitem__(self,key):
        h=self.__get_hash__(key)
        self.arr[h]=None
        
t=HashTable()

t['Shasha']=51
t['Harshitha']=27
t['Bavuma']=41

print(t['Harshitha'])

print(t.arr)
del t['Bavuma']
print(t.arr)
