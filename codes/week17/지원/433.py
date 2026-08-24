from collections import deque

class Solution(object):
    def canMutate(self, curr, target):
        count = 0
        
        for i in range(len(curr)):
            if curr[i] != target[i]:
                count += 1

                if count > 1:
                    return False

        return count == 1

    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        visited = [False for i in range(len(bank))]
        q = deque([(startGene, 0)])

        while q:
            currGen, count = q.popleft()
            if currGen == endGene:
                return count

            for i in range(len(bank)):
                if not visited[i] and self.canMutate(currGen, bank[i]):
                    visited[i] = True
                    q.append((bank[i], count + 1))
        
        return -1