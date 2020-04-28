class Solution:
	def sortColors(self,nums):
		if not nums or len(nums)==0:
			return 
		head=0
		now=0
		tail=len(nums)-1
		while now<tail:
			if nums[now]==1:
				now+=1
			elif nums[now]==0:
				nums[head],nums[now]=nums[now],nums[head]
				now+=1
				head+=1
			else:
				nums[tail],nums[now]=nums[now],nums[tail]
				tail-=1
