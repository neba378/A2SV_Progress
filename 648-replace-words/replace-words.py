class TrieNode:
    def __init__(self):
        self.is_end = False
        self.word = None
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
        cur.word = word

    def search(self, word: str) -> str:
        cur = self.root
        for ch in word:
            order = ord(ch)-ord("a")
            if cur.is_end:
                return cur.word
            if not cur.children[order]:
                return word
            cur = cur.children[order]
        if cur.is_end:
            return cur.word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        ans = []
        for word in dictionary:
            trie.insert(word)
        for word in sentence.split():
            ans.append(trie.search(word))
        print(ans)
        return " ".join(ans)