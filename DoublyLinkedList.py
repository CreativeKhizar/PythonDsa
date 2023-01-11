#	Doubly Linked List

class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
	
class LinkedList:
	def __init__(self):
		self.head=None
	
	def insert_at_begin(self,data):
		if self.head is None:
			self.head=Node(data)
		else:
			new_node=Node(data)
			new_node.next=self.head
			self.head.prev=new_node
			self.head=new_node
			
	def insert_at_end(self,data):
		if self.head is None:
			self.head=Node(data)
		else:
			itr=self.head
			while(itr.next!=None):
				itr=itr.next
			new_node=Node(data)
			itr.next=new_node
			new_node.prev=itr
	
	def insert_at_any_position(self,data,pos):
		if self.head is None:
			self.head=Node(data)
		else:
			i=0
			itr=self.head
			while(i<pos-1 and itr.next!=None):
				itr=itr.next
				i=i+1
			if i<pos-1:
				print("Not Possible")
			else:
				new_node=Node(data)
				new_node.next=itr.next
				new_node.prev=itr
				itr.next=new_node
				if new_node.next is not None:
					new_node.next.prev=new_node
			
	def traversal(self):
		if self.head is None:
			print("Empty Doubly Linked List")
		else:
			itr=self.head
			while itr is not None:
				print(itr.data,"<===>",end="")
				itr=itr.next
			print("NULL")
			
	def del_at_begin(self):
		if self.head is None:
			print("Linked list is empty operation not possible")
		else:
			self.head=self.head.next
			if self.head is not None:
				self.head.prev=None
				
	def del_at_end(self):
		if self.head is None:
			print("Linked list is empty operation not possible")
		else:
			itr=self.head
			while itr.next is not None:
				itr=itr.next
			itr=itr.prev
			itr.next=None
			
	def del_at_pos(self,pos):
		if self.head is None:
			print("Linked List is empty operation not posibble")
		else:
			itr=self.head
			i=0
			while i<pos-1 and itr.next is not None:
				itr=itr.next
				
			if i<pos-1:
				print("Operation not possible")
			else:
				new_node=itr.next
				itr.next=new_node.next
				new_node.next.prev=itr
			

sample=LinkedList()

t='y'

while(t=='y'):
	print("Enter your chocie to perform an operation on Doubly Linked List \n1 for Adding Node\n2 for Deleting the elements in the Doubly Linked List\n3 for Displaying the elements in Doubly Linked List")
	choice=int(input())
	if choice==1:
		print("Enter the data to insert")
		data=int(input())
		s=int(input("Enter 1 to add at beginning, 2 to add at end, 3 to add at any position : "))
		if s==1:
			sample.insert_at_begin(data) 
		elif s==2:
			sample.insert_at_end(data)
		elif s==3:
			index=int(input("Enter the index to add"))
			sample.insert_at_any_position(data,index)
		else:
			print("Invalid choice")
	
	elif choice==2:
		s=int(input("Enter 1 to delete the element at beginning, 2 for deleting at end, 3 to delete at any position : "))
		
		if s==1:
			sample.del_at_begin()
		elif s==2:
			sample.del_at_end()
		elif s==3:
			index=int(input("Enter the index to delete"))
			sample.del_at_pos(index)
		else:
			print("Invalid choice")
		
				
	elif choice==3:
		print("Elements in the Linked list are")
		sample.traversal()
	
	else:
		print("Invalid choice")
			
	n=input("if you want to continue press y else any other key: ")
	t=n
	


			
