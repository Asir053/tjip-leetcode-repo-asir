#O(n*m),O(n)
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
       

    def insert(self, word: str) -> None:
        temp = self.root
        
        for char in word:
            if not char in temp.children:
                temp.children[char] = TrieNode()
            
            temp = temp.children[char]
        
        temp.endOfWord = True
        

    def search(self, word: str, isPrefixSearch: bool = False) -> bool:
        temp = self.root
        
        for char in word:
            if char in temp.children:
                temp = temp.children[char]
            else:
                return False
        
        return temp.endOfWord or isPrefixSearch

    def startsWith(self, prefix: str) -> bool:       
        return self.search(prefix,True)
