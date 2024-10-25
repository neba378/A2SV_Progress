class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        i,j = 0,1
        folder.sort(key=lambda x: (x,len(x)))
        ans = []
        while j<len(folder):
            if folder[j].startswith(folder[i]) and folder[i]+'/' in folder[j]:
                j+=1
            else:
                ans.append(folder[i])
                i = j
                j+=1
        if i<len(folder):
            ans.append(folder[i])
        return ans