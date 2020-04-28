class Solution:
	def dailyTemperatures(self,T):
		if not T:
			return []
		n=len(T)
		stack=[]
		dist=[0]*n
		for i in range(n):
			while stack and T[stack[-1]]<T[i]:
				index=stack.pop()
				dist[index]=i-index
			stack.append(i)
		return dist
