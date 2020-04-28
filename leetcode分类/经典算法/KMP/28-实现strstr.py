class Solution:
	def strStr(self,haystack,needle):
		########暴力匹配#############
		  # https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-zhi-kmp-zi-fu-pi-pei-suan-fa
		M=len(needle)
		N=len(haystack)
		for i in range(N-M):
			for j in range(M+1): ###python不会最后自动加到M !!!!
				if j==M:
					return i
				if haystack[i]!==needle[j]:
					break
		return -1


##### KMP #############
class Solution:
	def strStr(self,haystack,needle):
        # dp[j][c] = next
        # 0 <= j < M，代表当前的状态
        # 0 <= c < 256，代表遇到的字符（ASCII 码）
        # 0 <= next <= M，代表下一个状态
        if needle=="":
        	return 0
        M=len(needle)
        dp=[[0]*256 for _ in range(M)]
        do[0][ord(needle[0])]=1
        X=0  ###影子状态

        def search(haystack,needle):
        	N=len(haystack)
        	j=0
        	for i in range(N):
        		j=dp[j][ord(haystack[i])]
        		if j==M:
        			return i-M+1
        	return -1
        #######
        for j in range(1,M):
        	for i in range(256):
        		if ord(needle[j])==i:
        			dp[j][i]=j+1
        		else:
        			dp[j][i]=dp[X][i]
        	X=dp[X][ord(needle[j])]

        return search(haystack,needle)

