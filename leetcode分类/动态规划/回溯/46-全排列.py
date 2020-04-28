class Solution:
	def permute(self,nums):
		self.result=[]
		if not nums:
			return self.result
		n=len(nums)
		self.backtrack(nums,0,n-1)
		return self.result

	def backtrack(self,nums,start,end):
		if start==end:
			self.result.append(copy.copy(nums))
			return

		for i in range(start,end+1):
			tmp=nums[i]
			nums[i]=nums[start]
			nums[start]=tmp
			self.backtrack(nums,start+1,end)
			tmp=nums[i]
			nums[i]=nums[start]
			nums[start]=tmp

#######################################
	def permute(self,nums):
        self.result=[]
        if not nums:
            return []
        self.length=len(nums)
        self.tmp=[0]*self.length
        self.backtrack(nums,0)
        return self.result

    def backtrack(self,nums,start):
        if start==self.length:
            self.result.append(self.tmp.copy())
            return

        for i in range(len(nums)):
            self.tmp[start]=nums[i]
            nums_1=nums[:i]+nums[i+1:]
            self.backtrack(nums_1,start+1)


