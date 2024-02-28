class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        counter = Counter(s[:k])
        count = 0
        
        for i,j in counter.items():
            if i in {'a','e','i','o','u'}:
                count+=j
        maxi = count
        for i in range(len(s)-k):
            if s[i] in {'a','e','i','o','u'}:
                count-=1
            if s[i+k] in {'a','e','i','o','u'}:
                count+=1
            maxi = max(maxi,count)
        return maxi
