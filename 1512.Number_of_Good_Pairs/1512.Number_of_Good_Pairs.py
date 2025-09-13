from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i<j and nums[i]==nums[j]:
                    c+=1
        return c