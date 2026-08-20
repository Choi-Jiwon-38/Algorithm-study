class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_dict = {}
        curr_idx = 0

        for i in range(n):
            curr_num = nums[i]

            if curr_num in num_dict:
                num_dict[curr_num] += 1
                
                if num_dict[curr_num] <= 2:
                    nums[curr_idx] = curr_num
                    curr_idx += 1
            
            else:
                num_dict[curr_num] = 1
                nums[curr_idx] = curr_num
                curr_idx += 1

        return curr_idx