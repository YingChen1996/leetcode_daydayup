class Solution:
	def maxProduxt(self,nums):
		if not nums:
			return 0
		n=len(nums)
		minnum=nums[0]
		maxnum=nums[0]
		result=nums[0]
		for i in range(1,n):
			tmp=minnum
			minnum=min(minnum*nums[i],maxnum*nums[i],nums[i])
			maxnum=max(tmp*nums[i],maxnum*nums[i],nums[i])
			result=max(result,maxnum)
		return result