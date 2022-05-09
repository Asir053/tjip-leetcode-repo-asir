##O(N) time & space
class Solution(object):
    def romanToInt(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for idx in range(len(s)-1,-1,-1):
            num = roman[s[idx]]
            if 4 * num < ans: ans -= num
            else: ans += num
        return ans
        
