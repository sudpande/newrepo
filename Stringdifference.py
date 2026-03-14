class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i, j = 0, 0
        sum_s = 0
        sum_t = 0
        while i < len(s):
            sum_s += ord(s[i])
            i += 1
        while j < len(t):
            sum_t += ord(t[j])
            j += 1
        return chr(sum_t - sum_s)