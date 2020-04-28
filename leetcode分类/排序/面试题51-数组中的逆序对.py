class Solution:
	def reversePairs(self,nums):
		if not nums:
			return 0
		n=len(nums)
		cpnums=nums.copy()
		cnt=self.mergeSort(nums,cpnums,0,n-1)
		return cnt

	def mergeSort(self,nums,cpnums,start,end):
		if start==end:
			cpnums[start]=nums[start]
			return 0
		mid=start+(end-start)//2
		left=self.mergeSort(cpnums,nums,start,mid)
		right=self.mergeSort(cpnums,nums,mid+1,end)

		cnt=0
		i=mid
		j=end
		index=end
		while i>=start and j>mid:
			if nums[i]>nums[j]:
				cpnums[index]=nums[i]
				cnt+=j-mid
				i-=1
			else:
				cpnums[index]=nums[j]
				j-=1
			index-=1
		while i>=start:
			cpnums[index]=nums[i]
			index-=1
			i-=1
		while j>mid:
			cpnums[index]=nums[j]
			index-=1
			j-=1
		return left+right+cnt

