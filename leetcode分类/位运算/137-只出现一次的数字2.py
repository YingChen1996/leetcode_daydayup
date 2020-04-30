class Solution:
	def singleNumber(self,nums):
		if not nums:
			return
		bitsum=[0]*32
		for num in nums:
			bit=1
			for j in range(31,-1,-1):
				tmp=num&bit
				if tmp!=0:
					bitsum[j]+=1
				bit<<=1
		result=0
		for i in range(32):
			result=result<<1
			result+=bitsum[i]%3

		if bitsum[0]%3==1:
			result-=4294967296              #numpy.power(2,32)
		return result