class Solution:
	def decodeString(self,s):
		self.stack=[]
        n=len(s)
        numlist=['0','1','2','3','4','5','6','7','8','9']
        for i in range(n):
            if s[i]!=']':
                self.stack.append(s[i])
            else:
                tmpstring=''
                while self.stack[-1]!='[':
                    tmpstring=self.stack.pop()+tmpstring
                self.stack.pop()

                tmpnumber=''
                while len(self.stack)>0 and self.stack[-1] in numlist:
                    tmpnumber=self.stack.pop()+tmpnumber
                tmpnumber=int(tmpnumber)
                string_final=tmpstring*tmpnumber
                self.stack.append("".join(string_final))
        return "".join(self.stack)

