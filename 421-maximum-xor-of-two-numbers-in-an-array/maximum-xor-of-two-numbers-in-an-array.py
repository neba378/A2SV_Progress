class TrieNode:
    def __init__(self):
        self.ind = None
        self.children = [None for _ in range(2)]
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def insert(self, word, i):
        cur = self.root
        for ch in range(len(word)):
            order = int(word[ch])
            if not cur.children[order]:
                cur.children[order] = TrieNode()
            cur = cur.children[order]
        cur.ind = i
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in range(len(word)):
            order = abs(int(word[ch])-1)
            order1 = int(word[ch])
            if not cur.children[order]:
                if cur.ind:
                    return cur.ind
                else:
                    cur = cur.children[order1]
                    continue
            cur = cur.children[order]
        return cur.ind

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tri = Trie()
        maxi = max(nums)
        m = len(bin(maxi)[2:])
        for i in range(len(nums)):
            b = bin(nums[i])[2:]
            nums[i] = (m-len(b))*"0"+b
        for i in range(len(nums)):
            tri.insert(nums[i],i)
        ans = 0
        for num in nums:
            ind = tri.search(num)
            ans = max(ans,int(num,2)^int(nums[ind],2))
        return ans