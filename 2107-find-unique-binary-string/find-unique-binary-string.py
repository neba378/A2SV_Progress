class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = set()
        for i in range(n):
            s.add(int(nums[i],2))
        mini = 0
        while mini < 2**n:
            if mini not in s:
                l = len(bin(mini))-2
                return (n-l)*'0'+bin(mini)[2:]
            mini+=1
        return -1
