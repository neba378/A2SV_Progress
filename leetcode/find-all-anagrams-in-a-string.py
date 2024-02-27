class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        counterP = Counter(p)
        
        ans = []
        for i in range(len(s)-len(p)+1):
            counterS = Counter(s[i:i+len(p)])
            if counterS==counterP:
                ans.append(i)
        return ans