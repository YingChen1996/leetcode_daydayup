class Solution:
	def merge(self,intervals):
		if not intervals:
			return []
		intervals=sorted(intervals, key=lambda x: x[0])
		left=intervals[0][0]
		right=intervals[0][1]
		n=len(intervals)
		result=[]
		for i in range(1,n):
			if intervals[i][0]<=right:
				right=max(right,intervals[i][1])
			else:
				result.append([left,right])
				left=intervals[i][0]
				right=intervals[i][1]
		result.append([left,right])
		return result