class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        lst = []
        dic = set()
        for i in arr2:
            for j in range(counter[i]):
                lst.append(i)
            dic.add(i)
        lst2 = []
        for i in arr1:
            if i not in dic:
                lst2.append(i)
        lst2.sort()
        lst.extend(lst2)
        return lst
