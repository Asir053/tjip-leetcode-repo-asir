class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        max = 1
        while r < len(s)-1:
            str = s[l:r+1]
            if s[r+1] not in str:
                str = str+ s[r+1]
                r += 1
                if len(str) > max:
                    max = len(str)
            else:
                l += 1
        if s == "":
            max = 0
        return max
        
