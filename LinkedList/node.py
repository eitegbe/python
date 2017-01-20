class Node(object):
	def __init__(self, a):
		self.a = a
		self.next = None

	def setNextNode(self, next):
		self.next = next

	def getNextNode(self):
		return self.next

	def setData(self, a):
		self.a = a

	def getData(self):
		return self.a 

	def __str__(self):
		return 'Value is: {}'.format(self.a)


class LinkedList(object):

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def insertNode(self, a):
		node = Node(a)
		if self.head is None:
			node.setNextNode(self.head)
			self.head = node
			self.tail = node
		else:
			self.tail.setNextNode(node)
			self.tail = node

	def display(self):
		if self.head is None and self.tail is None:
			print 'Empty'
			return
		else:
			current = self.head
			while current != None:
				print current
				current = current.getNextNode()

	def removeFirstNode(self):
		if self.head == None or self.tail == None:
			return None
		else:
			self.head = self.head.getNextNode()
			return self.head

	def removeLastNode(self):
		if self.head == self.tail:
			self.head = self.head.getNextNode()
			self.tail = self.tail.getNextNode()
			return self.tail
		else:
			current = self.head
			while current.getNextNode() != None:
				if current.getNextNode() ==  self.tail:
					current.setNextNode(None)
					self.tail = current
					break
				current = current.getNextNode()
		return self.head

	def reverseList(self):
		if self.head is None and self.tail is None:
			return 
		current = self.head
		prev = None
		while current:
			nextNode = current.getNextNode()
			current.setNextNode(prev)
			prev = current
			current = nextNode
		self.head = prev
		return self.head

	def add1(self):
		if self.head is None:
			return None

		current = self.head
		temp = None
		sums = 0
		carry = 1
		while current is not None:
			sums = current.getData() + carry
			carry = 1 if sums >= 10 else 0
			sums = sums % 10
			current.setData(sums)
			temp = current
			current = current.getNextNode()

		if carry > 0:
			temp.setNextNode(Node(carry))

		return self.head





if __name__ == '__main__':
	l = LinkedList()
	l.insertNode(9)
	l.insertNode(9)
	l.insertNode(9)
	l.insertNode(111)
	#l.display()
	l.removeLastNode()
	# l.removeLastNode()
	l.reverseList()
	l.add1()
	l.reverseList()
	l.display()

