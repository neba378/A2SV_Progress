class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        neg = 0
        for i in range(32):
            sumy=0
            for num in nums:
                if num<0:
                    neg+=1
                sumy+=(abs(num)>>i)&1
            sumy%=3
            if sumy!=0:
                sumy<<=i
                ans|=sumy
        if neg%3:
            return -ans
        return ans