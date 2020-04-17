class Solution:
	def superEggDrop(self,K,N):
		self.memo={}
		return self.dp(K,N)

	def dp(self,K,N):
		if (K,N) not in self.memo:
			if K==1:
				return N
			if N==0:
				return 0
			li=1
			hi=N
			while li+1<hi:
				X=(li+hi)//2
				t1=self.dp(K-1,X-1)
				t2=self.dp(K,N-X)
				if t1<t2:
					li=X
				elif t1>t2:
					hi=X
				else:
					li=hi=X
			result=1+min(max(self.dp(K-1,X-1),self.dp(K,N-X)) for X in [li,hi])
			self.memo[K,N]=result
		return self.memo[K,N]