class Solution:
	def singleNumber(self,nums):
		if not nums:
			return 
		result=0
		for num in nums:
			result^=num
		return result