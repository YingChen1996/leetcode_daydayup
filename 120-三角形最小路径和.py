class Solution:
	def minimumTotal(self,triangle):
        if not triangle:
            return 0
        ####自底向上dp
        n=len(triangle)
        for i in range(n-2,-1,-1):
            m=len(triangle[i])
            for j in range(m):
                triangle[i][j]=min(triangle[i+1][j],triangle[i+1][j+1])+triangle[i][j]
        return triangle[0][0]