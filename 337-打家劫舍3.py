class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

def Solution:
	def rob(self,root):
		res=self.dphelpper(root)
		return max(res)
		

	def dphelpper(self,root):
		ret=[0,0]
		if root is None:
			return ret 
		left=self.dphelpper(root.left)
		right=self.dphelpper(root.right)
		### not contain root
		ret[0]=max(left)+max(right)
		#### contain root
		ret[1]=left[0]+right[0]+root.val
		return ret


