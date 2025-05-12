class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def isGood(s):
            n = int(s)
            return not n%2 and len(str(n)) == 3
        ans = []
        dic = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=k and i!=j and j!=k:
                        num = str(digits[i])+str(digits[j])+str(digits[k])
                        if num not in dic and isGood(num):
                            ans.append(int(num))
                            dic.add(num)
        return sorted(ans)
