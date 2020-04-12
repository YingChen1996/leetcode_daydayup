class Solution:
	def lengthofLIS(self,nums):
		if not nums or len(nums)==0:
			return 0
		n=len(nums)
		dp=[1]*n
		for i in range(n):
			for j in range(i):
				if nums[j]<nums[i]:
					dp[i]=max(dp[i],dp[j]+1)
		return max(dp)
