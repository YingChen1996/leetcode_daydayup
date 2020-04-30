class Solution:
	def findErrorNums(self,nums):
		if not nums:
			return
		n=len(nums)
		for i in range(n):
			while nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
				tmp=nums[i]
				nums[i]=nums[tmp-1]
				nums[tmp-1]=tmp
		a,b=0,0
		for i in range(n):
			if nums[i]!=i+1:
				a=nums[i]
				b=i+1
				return [a,b]

