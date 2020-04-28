class Solution:
	def maxprofit(self,prices):
		if not prices:
			return 0
		minnum=prices[0]
		result=0
		n=len(prices)
		for i in range(1,n):
			if prices[i]<minnum:
				minnum=prices[i]
			else:
				result=max(result,prices[i]-minnum)
		return result