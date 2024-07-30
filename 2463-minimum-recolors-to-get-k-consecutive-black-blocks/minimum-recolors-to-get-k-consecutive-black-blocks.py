class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i,j = 0,k
        ans = len(blocks)
        while j<=len(blocks):
            ans = min(blocks[i:j].count("W"),ans)
            i+=1
            j+=1
        return ans