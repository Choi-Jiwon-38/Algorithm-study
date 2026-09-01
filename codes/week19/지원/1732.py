from collections import deque

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        height = deque([0])
        answer = 0

        for g in gain:
            new_value = height[-1] + g
            if new_value > answer:
                answer = new_value
            
            height.append(new_value)
        
        return answer
        