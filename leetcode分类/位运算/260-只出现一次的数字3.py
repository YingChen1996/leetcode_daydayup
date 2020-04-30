class Solution:
	def singleNumber(self,nums):
		if not nums:
			return 
		diff=0
		for num in nums:
			diff^=num
		diff=diff & ~(diff-1)
		ret=[0,0]
		for num in nums:
			if num&diff==0:
				ret[0]^=num
			else:
				ret[1]^=num 
		return ret
