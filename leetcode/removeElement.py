class Solution(object):

	def __init__(self):
		pass

	def renoveElement(self, nums, val):
		if nums is None or len(nums)==0:
			return 0
        
        begin = 0
        end = len(nums)-1
        while begin <= end:
            if nums[begin] != val:
                begin += 1
            
            elif nums[end] == val:
                end -= 1
            
            else:
                value = nums[begin]
                nums[begin] = nums[end]
                nums[end] = value
                begin += 1
                end -= 1
        return begin