class Solution:
	def canJump(self,nums):
		if not nums:
			return False
		n=len(nums)
		maxindices=0
		for i in range(n):
			if maxindices<i:
				return False
			maxindices=max(maxindices,nums[i]+i)
			if maxindices>=n-1:
				return True
		return maxindices>=n-1

