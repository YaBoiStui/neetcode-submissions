class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in letters_s:
                    letters_s[s[i]] += 1
                else:
                    letters_s[s[i]] = 1

            for n in range(len(t)):
                if t[n] in letters_t:
                    letters_t[t[n]] += 1
                else:
                    letters_t[t[n]] = 1
            
            if letters_s == letters_t:
                return True
                
        return False