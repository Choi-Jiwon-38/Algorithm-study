class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        sl = len(s)

        if sl == 0:
            return True

        for tc in t:
            if s[si] == tc:
                si += 1

                if si == sl:
                    return True

        return False