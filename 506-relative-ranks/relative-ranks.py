class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        temp = score[:]
        score_dict = {}
        temp.sort(reverse=True)
        ans = []
        for i in range(len(score)):
            score_dict[temp[i]] = i+1
        for num in score:
            if score_dict[num] == 1:
                ans.append("Gold Medal")
            elif score_dict[num] == 2:
                ans.append("Silver Medal")
            elif score_dict[num] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(score_dict[num]))
        return ans
            
