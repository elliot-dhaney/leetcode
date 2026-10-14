class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if (c in 'aeiou'):
                return True
        return False
    
# 0 vowels: alice loses
# > 0 odd vowels: take the whole string
# > 0 even vowels: alice takes all but one. guaranteed win


