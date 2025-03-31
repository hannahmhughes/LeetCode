class Solution:
    def climbStairs(self, n: int) -> int:

        # Base case 
        if n == 1: return 1

        # Initialize array to hold computed values 
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        # Compute for each position in array 
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        