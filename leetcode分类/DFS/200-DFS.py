class Solution:
	def numIslands(self,gird):
		if not grid:
            return 0
        self.n=len(grid)
        self.m=len(grid[0])
        cnt=0
        self.direction=[[0,1],[0,-1],[-1,0],[1,0]]
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    cnt+=1
        return cnt

    def dfs(self,grid,row,col):
        if row<0 or row>=self.n or col<0 or col>=self.m or grid[row][col]=='0':
            return 
        grid[row][col]='0'
        for d in self.direction:
            self.dfs(grid,row+d[0],col+d[1])
