
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = s.split()   # s.split() — splits the string by any amount of whitespace (spaces, tabs, etc.) and removes empty strings.
        x = L[-1]
        y = len(x)
        return y