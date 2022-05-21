##O(N) time & space
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        dictnry = {}

        for s_char, t_char in zip(s, t):
            dictnry[s_char] = t_char
        
        temp_str = ''
        for char in s:
            temp_str += dictnry[char]
        print(temp_str)
        
        return temp_str == t
        
