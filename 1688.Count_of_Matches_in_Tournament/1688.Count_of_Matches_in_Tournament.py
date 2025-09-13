class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        if n==1:
            return 0
        else:
            while n!=2:
                if n%2 == 0:
                    matches = n//2
                    n = n//2
                else:
                    matches = (n-1)//2
                    n = (n-1)//2 + 1
                total_matches+= matches
        return total_matches+1