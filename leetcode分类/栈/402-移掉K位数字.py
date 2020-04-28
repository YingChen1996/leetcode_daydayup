class Solution:
	def removeKdigits(self,nums,k):
		if not nums or len(nums)<=k:
			return ""
		if k==0:
			return nums
		n=len(nums)
		stack=[]
		cnt=0
		for c in nums:
			if len(stack)==0 or int(c)>=int(stack[-1]):
				stack.append(c)
			else:
				while stack and cnt<k and int(c)<int(stack[-1]):
					stack.pop()
					cnt+=1
				stack.append(c)

		while cnt<k:
			stack.pop()
			cnt+=1
		while stack and stack[0]=='0':
			stack.pop(0)

		return "".join(stack) if stack else '0'
