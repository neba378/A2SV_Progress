class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = nums[0]
        for i in nums[1:]:
            a^=i
        
        b = bin(a)[2:]
        k2 = bin(k)[2:]
        if len(b)>len(k2):
            k2 = "0"*(len(b)-len(k2))+k2
        else:
            b = "0"*(len(k2)-len(b))+b
        c = 0
        for i in range(len(k2)):
            if b[i]!=k2[i]:
                c+=1
        return c
