class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal 
        # s = goal+goal
        # def KMP_part_one(p : str) -> list:
        #     i,j = 0,1
        #     lsp = [0]*len(p)
        #     while j<len(p):
        #         if p[i] == p[j]:
        #             lsp[j] = i+1
        #             i+=1
        #             j+=1
        #         else:
        #             if i == 0:
        #                 j+=1
        #             else:
        #                 i = lsp[i-1]
        #     return lsp
        # lsp = KMP_part_one(s)
        # while j<len(goal):
        #     if s[i] == p[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         if i == 0:
        #             j+=1
        #         else:
        #             i = lsp[i-1]
        #     return 
