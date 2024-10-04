class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for ops in operations:
            if ops == "--X" or ops == "X--":
                ans-=1
            else:
                ans+=1
        return ans
