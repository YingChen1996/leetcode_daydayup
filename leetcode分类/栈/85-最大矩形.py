class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        height=[0]*m 
        maxarea=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='0':
                    height[j]=0
                else:
                    height[j]+=1
            area=self.maxrec(height)
            maxarea=max(maxarea,area)
        return maxarea

    def maxrec(self,height):
        stack=[-1]
        m=len(height)
        area=0
        for i in range(m):
            while len(stack)>1 and height[i]<=height[stack[-1]]:
                area=max(area,height[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)

        while len(stack)>1:
            area=max(area,height[stack.pop()]*(m-stack[-1]-1))
        return area