class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        answer = 0

        zero_count = nums.count(0)
    
        if zero_count <= 1:
            return l - 1

        def find_length(is_removed: bool, count: int, index: int, max_length: int):
            nonlocal answer            
            if nums[index] == 1:
                if index + 1 == max_length:
                    answer = max(answer, count + 1) 
                else:
                    find_length(is_removed, count + 1, index + 1, max_length)
            else:
                if is_removed:
                    answer = max(answer, count)
                else:
                    if index + 1 == max_length:
                        answer = max(answer, count) 
                    else:
                        find_length(True, count, index + 1, max_length)
                        find_length(False, 0, index + 1, max_length)
        
        find_length(False, 0, 0, l)

        return answer
