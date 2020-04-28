class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution:
	def mergeKLists(self,lists):
		if not lists:
			return
		n=len(lists)
		self.merge(lists,0,n-1)

	def merge(self,lists,start,end):
		if start==end:
			return lists[start]
		mid=start+(end-start)//2
		l1=self.merge(lists,start,mid)
		l2=self.merge(lists,mid+1,end)

		return self.merge2list(l1,l2)
		
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