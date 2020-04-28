class Solution:
	def isValid(self,s):
		if not s:
			return True
		stack=[]
		n=len(s)
		i=0
		while i<n:
			if s[i]=='(' or s[i]=='[' or s[i]=='{':
				stack.append(s[i])
			else:
				if len(stack)==0:
					return False
				c=stack.pop()
				b=s[i]==')' and c!='('
				d=s[i]==']' and c!='['
				e=s[i]=='}' and c!='{'
				if b or d or e:
					return False
			i+=1
		return len(stack)==0


