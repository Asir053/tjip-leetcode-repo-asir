class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def isSubseq(word):
            curr = 0
            for symbol in word:
                ind = bisect_left(places[symbol], curr)
                if ind >= len(places[symbol]):
                    return False
                curr = places[symbol][ind] + 1
            
            return True
        
        places = defaultdict(list)
        for i, symbol in enumerate(s):
            places[symbol].append(i)
        
        return sum(isSubseq(word) for word in words)
        
