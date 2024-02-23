class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chem = 0
        skill.sort()
        i = 0
        j = len(skill)-1
        sum = skill[-1]+skill[0]
        while(i<j):
            if skill[i]+skill[j] == sum:
                chem+=(skill[i]*skill[j])
                i+=1
                j-=1
            else:
                return -1
        return chem