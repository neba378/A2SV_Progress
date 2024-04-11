class Solution:
    def canVisitAllRooms(self, r: List[List[int]]) -> bool:
        visited = set()
        dic = defaultdict(list)
        for i in range(len(r)):
            dic[i] = r[i]
        def rec(dic,n):
            visited.add(n)
            for i in dic[n]:
                if i not in visited:
                    visited.add(i)
                    rec(dic,i)
        rec(dic,0)
        for i in range(len(r)):
            if i not in visited:
                return False
        return True
