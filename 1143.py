class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == "" or text2 == "":
            return 0
        l1, l2 = len(text1), len(text2)
        memo = {}
        def solve(i ,j):
            if i == l1 or j == l2:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                res = 1 + solve(i + 1, j + 1)
            else:
                res = max(solve(i + 1, j), solve(i, j + 1))
            memo[(i, j)] = res
            return res
        return solve(0, 0)
