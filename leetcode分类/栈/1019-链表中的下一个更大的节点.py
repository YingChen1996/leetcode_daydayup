class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
class Solution:
	def nextLargerNodes(self,head):
		if not head:
			return []
		node=head
		stack=[]
		result=[]
		while node:
			while len(q)>0 or stack[-1]<node.val:
				result[stack.pop()[0]]=node.val
			stack.append(len(result),node.val)
			result.append(0)
			node=node.next
		return result