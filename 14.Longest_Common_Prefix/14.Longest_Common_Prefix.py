from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        S = ""
        s = strs[0][:2]
        for i in strs:
            if i[:2] != s:
                return S
        S = S + s
        return S

            
        