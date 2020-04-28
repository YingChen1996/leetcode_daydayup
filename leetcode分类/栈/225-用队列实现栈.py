import collections
class Mystack:
	def __init__(self):
		self.q=collections.deque()

	def push(self,val):
		self.q.append(val)
		for _ in range(len(self.q)-1):
			self.q.append(self.q.popleft())

	def pop(self):
		if self.q:
			return self.q.popleft()

	def top(self):
		if self.q:
			return self.q[0]

	def empty(self):
		return not len(self.q)
