class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst = (s1+" "+s2).split()
        counter = Counter(lst)
        ans = []
        for i,j in counter.items():
            if j ==1:
                ans.append(i)
        return ans