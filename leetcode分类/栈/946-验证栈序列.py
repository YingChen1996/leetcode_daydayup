class Solution:
	def validateStackSequence(self,pushed,popped):
        if not pushed and not popped:
            return True
        stack=[]
        while pushed or popped or stack:
            if stack and stack[-1]==popped[0]:
                stack.pop()
                popped.pop(0)
                continue
            if pushed:
                stack.append(pushed.pop(0))
            if stack[-1]!=popped[0] and len(pushed)==0:
                return False
        return len(stack)==0
