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
	tree.insert(8)
	tree.insert(11)
	tree.insert(6)
	tree.preorder()



