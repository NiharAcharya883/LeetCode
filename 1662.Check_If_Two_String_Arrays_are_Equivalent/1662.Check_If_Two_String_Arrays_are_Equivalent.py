from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        complete_word1 = "".join(word1)
        complete_word2 = "".join(word2)
        if complete_word1 == complete_word2:
            return True
        else:
            return False