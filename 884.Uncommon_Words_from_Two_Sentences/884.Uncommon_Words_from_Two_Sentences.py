class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        L1 = s1.split()
        L3 =[]
        L2 = s2.split()
        for i in L1:
            if i not in L2 and L1.count(i)==1:
                L3.append(i)
        for i in L2:
            if i not in L1 and L2.count(i)==1:
                L3.append(i)
        return L3
        