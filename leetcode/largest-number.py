class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            if a+b > b+a:
                return 1
            elif b+a>a+b:
                return -1
            return 0
        lst = []
        for i in nums:
            lst.append(str(i))
        lst.sort(key=cmp_to_key(compare),reverse=True)
        s = "".join(lst)
        if s[0] == "0":
            return "0"
        return s