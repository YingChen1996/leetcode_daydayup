class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution:
	def inorderTraversal(self,root):
		if not root:
			return []
		stack=[]
		node=root
		result=[]
		while stack or node:
			while node:
				stack.append([node,1])
				node=node.left
			if stack and stack[-1][1]==2:
				stack.pop()
			if stack and stack[-1][1]==1:
				result.append(stack[-1][0].val)
				stack[-1][1]=2
				node=stack[-1][0].right
		return result


