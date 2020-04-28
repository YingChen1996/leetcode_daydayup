class Solution:
	def maxProfit(self,k,prices):
		if not prices:
			return 0
		n=len(prices)
		if k>=n//2:
			profit=0
			for i in range(1,n):
				if prices[i]-prices[i-1]>0:
					profit+=prices[i]-prices[i-1]
			return profit
		else:
			dp=[[[0]*2 for _ in range(k+1)] for _ in range(n)]
