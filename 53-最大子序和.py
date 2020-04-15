class Solution:
	def maxSubArray(self,nums):
		if not nums:
			return 0
		n=len(nums)
		maxnum=nums[0]
		currnum=nums[0]
		for i in range(1,n):
			if currnum<0:
				currnum=nums[i]
			else:
				currnum+=nums[i]
			maxnum=max(maxnum,currnum)
		return maxnum
