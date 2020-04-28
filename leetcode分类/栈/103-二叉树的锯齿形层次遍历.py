class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
	def Solution:
		def zigzagLevelOrder(self,root):
			stack=[]
			if not root:
				return stack
			cur=0
			curnode=[root]
			while curnode:
				nextnode=[]
				tmpval=[]
				while curnode:
					tmpnode=curnode.pop()
					tmpval.append(tmpnode.val)
					if cur==0:
						if tmpnode.left:
							nextnode.append(tmpnode.left)
						if tmpnode.right:
							nextnode.append(tmpnode.right)
					else:
						if tmpnode.right:
							nextnode.append(tmpnode.right)
						if tmpnode.left:
							nextnode.append(tmpnode.left)
				if tmpval:
					stack.append(tmpval)
				curnode=nextnode
				cur=1-cur
			return stack



