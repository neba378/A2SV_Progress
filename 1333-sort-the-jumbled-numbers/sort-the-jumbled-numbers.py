class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            n = ""
            for each in str(nums[i]):
                n+=str(mapping[int(each)])
            ans.append([int(n),i,nums[i]])
        ans.sort()
        final = [num for ord,ind,num in ans]
        return final
        
