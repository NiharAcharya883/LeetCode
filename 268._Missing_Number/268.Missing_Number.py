from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Missing number = (Total sum of numbers from 0-n) - (sum of array)
        # sum of numbers from 0 to n = n * (n+1) // 2
        l = len(nums)
        total_sum = l * (l+1) // 2
        array_sum = sum(nums)
        mn = total_sum - array_sum
        return mn 