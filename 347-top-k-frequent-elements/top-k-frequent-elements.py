class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        dic = defaultdict(list)
        for i,j in counter.items():
            dic[j].append(i)
        
        keys = dic.keys()
        most = nlargest(k,keys)
        ans = []
        for i in most:
            if len(ans)<k:
                for j in dic[i]:
                    if len(ans)<k:
                        ans.append(j)
                    else:
                        break
            else:
                break
        
        return ans