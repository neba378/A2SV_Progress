class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        dic = {}
        for k,v in counter.items():
            if v>=3:
                if v%2:
                    dic[k] = 1
                else:
                    dic[k] = 2
            else:
                dic[k] = v
        return sum(dic.values())