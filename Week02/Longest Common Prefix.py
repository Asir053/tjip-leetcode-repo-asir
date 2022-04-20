class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1: return ""
        min_word, max_word = strs[0], strs[0]
        for w in strs:
            if min_word > w: min_word = w
            if max_word < w: max_word = w
        
        iterations = min(len(min_word), len(max_word))
        result = 0
        for i in range(iterations):
            if min_word[i] == max_word[i]:
                result += 1
            else: return min_word[:result]
        return min_word[:result]
