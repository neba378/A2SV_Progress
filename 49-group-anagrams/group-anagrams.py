class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for each in strs:
            lst = [i for i in each]
            lst.sort()
            sorted_str = "".join(lst)
            dic[sorted_str].append(each)
        return list(dic.values())