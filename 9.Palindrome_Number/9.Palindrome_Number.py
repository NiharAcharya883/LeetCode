class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        s = x
        if x<0:
            return False
        else:
            while s!=0:
                rem = s%10
                rev = rev*10 + rem
                s = s//10
            if rev == x:
                return True
            else:
                return False
        