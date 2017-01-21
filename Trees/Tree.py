class Node(object):
	def __init__(self, data, leftChild=None, rightChild=None):
		self.data = data
		self.leftChild = leftChild
		self.rightChild = rightChild

	def setLeftChild(self, leftChild):
		self.leftChild = leftChild

	def setRightChild(self, rightChild):
		self.rightChild = rightChild

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def __str__(self):
		return "Value is {}".format(self.getData())


class Tree(object):

	def __init__(self):
		self.root = None

	def insert(self, data):
		self.root = self.insertNode(self.root, data)

	def insertNode(self, root, data):
		if root is None:
			root = Node(data)
		elif root.getData() < data:
				root.setRightChild(self.insertNode(root.getRightChild(), data))
		elif root.getData() > data:
				root.setLeftChild(self.insertNode(root.getLeftChild(), data))
		else:
			root.setData(data)
		return root

	def iterInsert(self, data):
		node = Node(data)
		if self.root is None:
			self.root = node
		else:
			self.root = self.iterInsertNode(self.root, data)

	def iterInsertNode(self, root, data):
		if root is None:
			return None

		current = root
		previous = None
		
		while current is not None:
			previous = current
			if current.getData() < data:
				current = current.getRightChild()
			else:
				current = current.getLeftChild()

		if previous.getData() < data:
			previous.setRightChild(Node(data))
		else:
			previous.setLeftChild(Node(data))
			
		return root

	def preorder(self):
		self.preorders(self.root)

	def preorders(self, root):
		if root is None:
			return
		else:
			print root
			self.preorders(root.getLeftChild())
			self.preorders(root.getRightChild())
	
if __name__=="__main__":
	tree = Tree()
	tree.iterInsert(8)
	tree.iterInsert(11)
	tree.iterInsert(6)
	tree.preorder()



