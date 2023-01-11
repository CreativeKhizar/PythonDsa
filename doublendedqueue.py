class Deque:
    def __init__(self):
        self.queue = []
        self.count = 0
    def __repr__(self):
        str = ""
        if self.count == 0:
            str += "Double Ended Queue Empty."
            return str
        str += "Double Ended Queue:\n" + self.queue.__repr__()
        return str
    def insert_start(self,data):
        if self.count == 0:
            self.queue = [data,]
            self.count = 1
            return
        self.queue.insert(0,data)
        self.count += 1
        return
    def insert_end(self,data):
        if self.count == 0:
            self.queue = data
            self.count = 1
            return
        self.queue.append(data)
        self.count += 1
        return
    def remove_start(self):
        if self.count == 0:
            raise ValueError("Invalid Operation")
        x = self.queue.pop(0)
        self.count -= 1
        return x
    def remove_end(self):
        if self.count == 0:
            raise ValueError("Invalid Operation")
        x = self.queue.pop()
        self.count -= 1
        return x
    def display(self):
        for i in self.queue:
            print(i, end=" ")
        print()
DQ = Deque()
ch = None
while True:
    print("1: Insert at start 2: Insert at end 3: Remove at start 4: Remove at end 5: Display 6 :Exit")
    ch = int(input("Enter the choice : "))
    if ch ==1:
        item = int(input("Enter element to be inserted : "))
        DQ.insert_start(item)
    elif ch ==2:
        item3 = int(input("Enter element to be inserted : "))
        DQ.insert_end(item3)
    elif ch==3:
        DQ.remove_start()
    elif ch==4:
        DQ.remove_end()
    elif ch ==5:
        DQ.display()
    elif ch ==6:
        break
    else:
        print("Invalid Choice ")
        
