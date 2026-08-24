class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_str = str(x)
        i = 0
        j = len(x_str) - 1

        while i < j:
            if x_str[i] == x_str[j]:
                i += 1
                j -= 1
            else:
                return False

        return True