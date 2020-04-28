class ListNode:
	def __init__(self,x):
		self.x=x
		self.next=None

class Solution:
	def mergeTwoLists(self,l1,l2):
		if l1 is None:
			return l2
		if l2 is None:
			return l1
		merge=None
		if l1.val<l2.val:
			merge=l1
			merge.next=self.mergeTwoLists(l1.next,l2)
		else:
			merge=l2
			merge.next=self.mergeTwoLists(l1,l2.next)
		return merge
