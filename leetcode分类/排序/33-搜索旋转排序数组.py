class Solution:
	def search(self,nums,target):
		if not nums:
			return -1
		n=len(nums)
		left=0
		right=n-1
		while left<right:
			mid=left+(right-left)//2
			if nums[mid]==target:
				return mid
			elif nums[mid]<nums[start]: ###右边有序  不取等号
				if nums[mid]<target and target<=nums[right]:
					left=mid+1
				else:
					right=mid-1
			else:
				if nums[mid]>target and target>=nums[left]: #####中间值大于左值，左边有序
					right=mid-1
				else:
					left=mid+1
		return left if nums[left]==target else -1


