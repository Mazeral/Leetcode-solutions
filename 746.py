
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0] * len(cost)
        dp[0] = cost[0]
        i = 1
        while i < len(cost) - 1:
            if i == 1:
                dp[i] = min(cost[i], dp[i - 1] + cost[i + 1])
            elif dp[i - 1] + cost[i] < dp[i - 2] + cost[i + 1]:
                dp[i] = dp[i - 1] + cost[i]
            else:
                dp[i] = dp[i - 2] + cost[i + 1]
            i += 1
        return dp[-1]
