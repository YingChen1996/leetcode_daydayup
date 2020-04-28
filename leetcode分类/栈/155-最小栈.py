class MinStack:
	def __init__(self):
		self.stack=[]
		self.aff=[]

	def push(self,x):
		self.stack.append(x)
		if len(self.aff)==0 or x<self.aff[-1]:
			self.aff.append(x)
		else:
			self.aff.append(self.aff[-1])

	def pop(self):
		if len(self.stack)>0 and len(self.aff)>0:
			self.stack.pop()
			self.aff.pop()

	def top(self):
		if len(self.stack)>0:
			return self.stack[-1]

	def getMin(self):
		if len(self.stack)>0:
			return self.aff[-1]