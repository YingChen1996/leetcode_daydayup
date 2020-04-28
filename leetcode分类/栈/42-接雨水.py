class Solution:
	def trap(self,height):
		if not height:
			return 0
		n=len(height)
		left=[0]*n
		right=[0]*n 
		maxx=0
		for i in range(n):
			maxx=max(maxx,height[i])
			left[i]=maxx
		maxx=0
		for i in range(n-1,-1,-1):
			maxx=max(maxx,height[i])
			right[i]=maxx
		area=0
		for i in range(n):
			area+=min(left[i],right[i])-height[i]
		return area


