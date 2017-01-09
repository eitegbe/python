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
		if self.head is None or self.tail is None:
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





if __name__ == '__main__':
	l = LinkedList()
	l.insertNode(2)
	l.insertNode(3)
	l.insertNode(10)
	l.insertNode(111)
	l.display()
	l.removeLastNode()
	l.removeLastNode()
	l.display()
