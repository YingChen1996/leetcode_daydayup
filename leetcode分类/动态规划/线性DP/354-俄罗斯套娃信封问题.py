class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        ###排序+最长递增子序列,超时
        # if not envelopes:
        #     return 0
        # envelopes=sorted(envelopes,key=lambda x: (x[0],x[1]))
        # n=len(envelopes)
        # dp=[1]*n
        # for i in range(n):
        #     for j in range(i):
        #         if envelopes[j][0]<envelopes[i][0] and envelopes[j][1]<envelopes[i][1]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)

        ###参考官方解答, 及leetcode 300. 最长上升子序列 二分法解决方案
        if not envelopes:
            return 0
        envelopes=sorted(envelopes,key=lambda x: (x[0],-x[1]))
        n=len(envelopes)
        dp=[0]*n
        length=0
        for num in envelopes:
            index=self.binary(dp,length,num)
            dp[index]=num[1]
            if index==length:
                length+=1
        return length

    def binary(self,dp,length,num):
        l=0
        h=length
        while l<h:
            mid=(l+h)//2
            if dp[mid]==num[1]:
                return mid
            elif dp[mid]<num[1]:
                l=mid+1
            else:
                h=mid
        return l
