class Solution:
    def frequencySort(self, s: str) -> str:
        lst = [i for i in s]
        counter = Counter(lst)
        a = sorted(lst,key=lambda x: (counter[x],x),reverse=True)
        return "".join(a)