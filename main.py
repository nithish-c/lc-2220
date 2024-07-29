class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        s = f"{xor:b}"
        result = 0
        for i in range(len(s)):
            if s[i] == '1':
                result += 1
        return result

sol = Solution()
print(sol.minBitFlips(10, 7))
