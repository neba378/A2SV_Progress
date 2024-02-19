class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = [(name, height) for name, height in zip(names, heights)]
        lst.sort(key=lambda x:x[1])
        lst2 = []
        for i in range(len(lst)-1, -1, -1):
            lst2.append(lst[i][0])
        
        return lst2