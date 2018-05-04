class Solution:
	def twoSum(self,nums,target):
	"""
	type nums:list[int]
	type target::int
	rtypr List[int]
	思路：首先判断给定的数组元素是否小于等于1
	其次将目标和与数组元素的差存入临时字典，同时将该元素的位置作为该键的value存入。判断其余的元素是否在临时字典中，若存在，则说明有两个元素的和是目标和，返回他们的位置信息存放在数组中。
	"""
	if len(nums) <= 1:
		return Flase
	buff_dict = {}
	for i in range(len(nums)):
		if nums[i] in buff_dict:
			return [buff_dict[nums[i],i]
		else:
			buff_dict[target - nums[i]] = i
