class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        if len(costs) == 0:
            return None
        
        lastR, lastG, lastB = costs[0][:]

        for i in range(1, len(costs)):
            curR = min(lastG, lastB) + costs[i][0]
            curG = min(lastR, lastB) + costs[i][1]
            curB = min(lastR, lastG) + costs[i][2]
            lastR, lastG, lastB = curR, curG, curB
        
        return min(min(lastR, lastG), lastB)

#DP
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        dp = [0, 0, 0]

        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]
        
        return min(dp)