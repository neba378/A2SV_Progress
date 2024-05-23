class TrieNode:
    def __init__(self, is_end = False):
        self.children = [None for _ in range(26)]
        self.is_end = is_end
class Trie:
    def __init__(self):
        self.root = TrieNode(True)

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
            if not cur.is_end:
                return False
            cur = cur.children[order]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(reverse=True)
        words.sort(key=lambda x: len(x))
        trie = Trie()
        for word in words:
            trie.insert(word)

        for word in words[::-1]:
            if trie.search(word):
                return word
        return ""

            