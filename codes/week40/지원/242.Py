class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        count1 = dict()
        count2 = dict()

        cnt1 = 0
        cnt2 = 0

        for c1 in s:
            cnt1 += 1
            if c1 in count1:
                count1[c1] += 1
            else:
                count1[c1] = 1

        
        for c2 in t:
            cnt2 += 1
            if c2 in count2:
                count2[c2] += 1
            else:
                count2[c2] = 1

        flag = True

        if cnt1 != cnt2:
            return False

        for key in list(count1.keys()):
            if key not in count2 or count1[key] != count2[key]:
                flag = False
                break
        
        return flag