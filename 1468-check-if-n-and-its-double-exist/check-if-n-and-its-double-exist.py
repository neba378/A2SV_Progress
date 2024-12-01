class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cz = arr.count(0)
        arr = set(arr)
        for n in arr:
            if 2*n in arr:
                if n == 0:
                    if cz>1:
                        return True
                else:
                    return True
                
        return False