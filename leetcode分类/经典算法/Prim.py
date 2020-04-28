class Solution:
	def __init__(self,G):
		self.G=G
		self.n=len(G)
		self.adjvex=[0]*self.n    ### node index
		self.lowcost=[0]*self.n    ### U-> V-U  minninum edge
		for i in range(self.n):   ###initialization
			self.adjvex[i]=0
			self.lowcost[i]=self.G[0][i]
		self.lowcost[0]=0

	def mininum(self,):
		minval=float('inf')
		k=0
		for i in range(self.n):
			if self.lowcost[i]!=0 and self.lowcost<minval:
				minval=self.lowcost[i]
				k=i
		return k

	def Prim(self,):
		for i in range(1,self.n):
			k=self.mininum()
			self.lowcost[k]=0
			for j in range(self.n):
				if self.lowcost[j]!=0 and self.G[k][j]<self.lowcost[j]:
					self.lowcost[j]=self.G[k][j]





