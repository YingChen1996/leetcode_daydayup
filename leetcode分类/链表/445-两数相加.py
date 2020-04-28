class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution:
	def addTwoNumbers(self,l1,l2):
		if not l1:
			return l2
		if not l2:
			return l1
		stack1=[]
		stakc2=[]
		node=l1
		while node:
			stack1.append(node.val)
			node=node.next
		node=l2:
		while node:
			stakc2.append(node.val)
			node=node.next
		dummyhead=ListNode(0)
		node=dummyhead
		cur=0
		while stack1 or stakc2 or cur!=0:
			l1=stack1.pop() if stack1 else 0
			l2=stakc2.pop() if stakc2 else 0
			tmpsum=l1+l1+cur
			cur=tmpsum//10
			node=ListNode(tmpsum%10)
			node.next=dummyhead.next ######### Attention
			dummyhead.next=node   ########
		return dummyhead.next
