class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [None for i in range(38)]
        
        # Base case
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        if n < 3:
            return dp[n]

        # Recursion Case
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]