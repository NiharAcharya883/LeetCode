class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = len(word) - 1
        try:
            ind = word.index(ch)
            s = ""
            for i in range(l,ind,-1):
                s = s + word[i]
            for i in range(0,ind+1):
                s = s + word[i]
            return s[::-1]
        except:
            return word
