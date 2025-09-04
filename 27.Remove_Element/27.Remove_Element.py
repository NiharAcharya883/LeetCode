from typing import List
# Use 2 pointers - somewhatdifficult.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[x] = nums[i]
                x = x + 1
        return x
        
                
        
        