class Solution:
	def twoSum(self,nums,target):
	"""
	type nums:list[int]
	type target::int
	rtypr List[int]
	"""
	if len(nums) <= 1:
		return Flase
	buff_dict = {}
	for i in range(len(nums)):
		if nums[i] in buff_dict:
			return [buff_dict[nums[i],i]
		else:
			buff_dict[target - nums[i]] = i
