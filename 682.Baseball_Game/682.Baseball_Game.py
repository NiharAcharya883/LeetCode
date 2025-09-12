from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L = []
        for i in operations:
            if i == "C":
                L.pop()
            elif i == "+":
                a = L.pop()
                b = L.pop()
                c = a + b
                L.append(b)
                L.append(a)
                L.append(c)
            elif i == "D":
                a = L.pop()
                L.append(a)
                L.append(a*2)
            else:
                L.append(int(i))
        s = sum(L)
        return s

            