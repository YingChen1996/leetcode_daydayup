class Solution:
	def maxProfit(self,prices):
		if not prices:
			return 0
		dp_i_0=0
		dp_i_1=float('-inf')
		n=len(prices)
		for i in range(n):
			tmp=dp_i_0
			dp_i_0=max(dp_i_0,dp_i_1+prices[i])
			dp_i_1=max(dp_i_1,tmp-prices[i])
		return dp_i_0

		############
		profit=0
		n=len(prices)
		for i in range(1,n):
			if prices[i]-prices[i-1]>0:
				profit+=prices[i]-prices[i-1]
		return profit