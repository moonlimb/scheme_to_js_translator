# a binary search tree (BST) -- ordered binary tree

# Properties:
#	- node.key >= node.left.key
#	- node.key <= node.right.key
#	- no duplicate nodes --> each node unique
#	- all subtress also BST

# binary tree != BST **

# insert
# lookup
# traversal: in-order, pre-order, post-order

class Node:
	left, right, data = None, None, None
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class BinarySearchTree:
	def __init__(self):
		self.root = None
		# why?
	#def print_tree(self):
	
	# calculate why O(n) = log(n) / worst vs. best case
	def find_node(self, target):
		if target == self.data return True
		elif target < self.data:
			return find_node(self.left)
		else:
			return find_node(self.right)
		return False	
# def lookup(self, root, target)
# def insert(self, root, target)
# def addnode(self, data)

# def get_depth
# def print_tree()
