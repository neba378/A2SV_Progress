class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(27)]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            order = ord(ch)-ord("a")
            if not cur.children[order]:
                cur.children[order] = TrieNode()
            cur = cur.children[order]
        cur.is_end = True



    def search(self, word: str) -> bool:
        return self.dfs(word,self.root)
    def dfs(self,word,node):
        cur = node
        for i in range(len(word)):
            if word[i] == ".":
                for child in cur.children:
                    if child and self.dfs(word[i+1:],child):
                        return True
                return False
            order = ord(word[i])-ord("a")
            if not cur.children[order]:
                return False
            cur = cur.children[order]
        if cur.is_end:
            return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)