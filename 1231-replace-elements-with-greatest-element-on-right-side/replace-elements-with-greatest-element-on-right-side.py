class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0
        ans = [-1]
        for i in range(len(arr)-1,-1,-1):
            m = max(m,arr[i])
            ans.append(m)
        ans.reverse()
        return ans[1:]
