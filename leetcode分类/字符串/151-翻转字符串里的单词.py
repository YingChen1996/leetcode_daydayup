##### convert to list
class Solution:
	def reverseWords(self,s):
		if s is None or len(s)==0:
			return s
		s=s.split()
		start=0
		end=len(s)-1
		while start<end:
			s[start],s[end]=s[end],s[start]
			start+=1
			end-=1
		return " ".join(s)
###############################遍历法空格判断
class Solution:
	def reverseWords(self,s):
		s=' '.join(s.split())
		if s is None or len(s)==0:
			return s
		n=len(s)
		start=0
		end=0
		self.s=s
		self.reverse(start,end)
		while end<n:
			if end<n and self.s[end]!=" ":
				end+=1
			else:
				self.reverse(start,end-1)
				end+=1
				start=end 
		return self.s

	def reverse(self,start,end):
		while start<end:
			tmp=self.s[start]
			self.s=self.s[:start]+self.s[end]+self.s[start+1:]
			self.s=self.s[:end]+tmp+self.s[end+1:]
			start+=1
			end-=1

