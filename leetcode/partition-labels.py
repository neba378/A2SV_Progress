class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)
        for ind,ch in enumerate(s):
            if ch in dic:
                dic[ch][1] = ind
            else:
                dic[ch].append(ind)
                dic[ch].append(ind)
        start = 0
        end = dic[s[0]][1]
        ans = []
        for ch in dic:
            s = dic[ch][0]
            e = dic[ch][1]
            if s>end:
                ans.append(end-start+1)
                end = e
                start = s
            end = max(e,end)
        ans.append(end-start+1)
        return ans
        