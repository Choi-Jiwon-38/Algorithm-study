class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = -1
        curr_num = None
        n = len(nums)

        for num in nums:
            if num != curr_num:
                curr_num = num
                curr_idx += 1
                nums[curr_idx] = curr_num

        return curr_idx + 1