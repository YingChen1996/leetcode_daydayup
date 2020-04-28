class Solution:
	def rob(self,nums):
		if not nums or len(nums)==0:
			return 0
		n=len(nums)
		if n==1:
			return nums[0]
		return max(self.rob_1(nums[:n-1]),self.rob_1(nums[1:]))


	def rob_1(self,nums):
		if not nums:
			return 0
		prev2=0
		prev1=nums[0]
		n=len(nums)
		i=1
		money=nums[0]
		while i<n:
			money=max(prev2+nums[i],prev1)
			prev2=prev1
			prev1=money
			i+=1
		return money
