class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            if trust == []:
                return 1
        dic = defaultdict(set)
        count = defaultdict(int)
        for a,b in trust:
            dic[b].add(a)
            count[a]+=1
        for i,j in dic.items():
            if len(j) == n-1 and count[i]==0:
                return i
        return -1