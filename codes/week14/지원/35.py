class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        if target <= nums[0]:
            return 0 

        if target > nums[-1]:
            return n
        
        for i in range(1, n):
            if nums[i - 1] <= target and target <= nums[i]:
                return i