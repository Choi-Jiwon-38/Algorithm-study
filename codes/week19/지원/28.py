class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                flag = True
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        flag = False
                        break
            
                if flag:
                    return i
        
        return -1
        