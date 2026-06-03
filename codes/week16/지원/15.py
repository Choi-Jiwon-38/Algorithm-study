class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        num_dict = dict()
        nums.sort()
        answer_keys = dict()

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
    
        if len(num_dict) == 1:
            if 0 in num_dict:
                return [[0, 0, 0]]
            else:
                return []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 1):
                target = -1 * (nums[i] + nums[j])
                selected_dict = dict()

                if not target in num_dict:
                    continue
                
                for selected in [nums[i], nums[j], target]:
                    if selected in selected_dict:
                        selected_dict[selected] += 1
                    else:
                        selected_dict[selected] = 1

                can_make = True

                for key in list(selected_dict.keys()):
                    if num_dict[key] < selected_dict[key]:
                        can_make = False
                        break
                
                if can_make:
                    key = tuple(sorted([nums[i], nums[j], target]))

                    if not key in answer_keys:
                        answer.append([nums[i], nums[j], target])
                        answer_keys[key] = True
                
        return answer