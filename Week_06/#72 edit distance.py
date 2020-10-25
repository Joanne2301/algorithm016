class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m

        Dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            Dp[i][0] = i
        for j in range(m + 1):
            Dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = Dp[i - 1][j] + 1
                down = Dp[i][j - 1] + 1
                leftDown = Dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    leftDown += 1
                Dp[i][j] = min(left, down, leftDown)

        return Dp[n][m]