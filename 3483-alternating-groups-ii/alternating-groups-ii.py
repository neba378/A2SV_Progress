class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # def alternates(nums):
        #     c = 0
        #     i = 0
        #     while i<len(nums)-1:
        #         if nums[i]==nums[i+1]:
        #             return 0
        #         i+=1
        #     # print(nums)
        #     return 1
        # ans = 0
        # for i in range(len(colors)-k+1):
        #     if alternates(colors[i:i+k]):
        #         ans+=1
        # circleList = colors[len(colors)-k+1:]+colors[:k-1]
        # # print(circleList)
        # for i in range(len(circleList)-k+1):
        #     if alternates(circleList[i:i+k]):
        #         ans+=1
        # return ans
        def countAlternate(colors):
            j = 0
            i = 0
            ans = 0
            while j<len(colors)-1:
                if colors[j] == colors[j+1]:
                    i = j+1
                j+=1
                if j-i+1 == k:
                    i+=1
                    ans+=1
            if j-i+1 == k:
                ans+=1
            return ans
        tot = 0
        circleList = colors[len(colors)-k+1:]+colors[:k-1]
        print(circleList)
        tot+=countAlternate(colors)
        tot+=countAlternate(circleList)
        return tot
