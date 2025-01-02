class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowels = "aeiou"
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])
        ans = []
        for query in queries:
            ans.append(prefix[query[1]+1]-prefix[query[0]])
        return ans

