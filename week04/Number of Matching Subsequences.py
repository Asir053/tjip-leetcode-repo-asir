#O(n*m),O(n)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def insert(word: str):
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            if None in curr:
                curr[None] += 1  
            else:
                curr[None] = 1
            
        len_s = len(s)
        trie = {}
        for word in words:
            insert(word)
        res = 0

        queue = [(trie, 0)]
        while queue:
            curr, match_idx = queue.pop()
            for char in curr:
                if char == None:
                    res += curr[None]
                else:
                    for idx in range(match_idx, len_s):
                        if s[idx] == char:
                            queue.append((curr[char], idx + 1))
                            break
        return res
        
