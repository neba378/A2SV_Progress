class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)] 

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            order = ord(ch)-ord("a")
            if not cur.children[order]:
                cur.children[order] = TrieNode()
            cur = cur.children[order]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            order = ord(ch)-ord("a")
            if not cur.children[order]:
                return False
            cur = cur.children[order]
        if cur.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            order = ord(ch)-ord("a")
            if not cur.children[order]:
                return False
            cur = cur.children[order]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)