class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        bitmask = 0
        first_occurrence = {0: -1} 
        max_length = 0
        
        for i, char in enumerate(s):
            if char in vowel_map:
                bitmask ^= (1 << vowel_map[char])
            
            if bitmask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                first_occurrence[bitmask] = i
        
        return max_length