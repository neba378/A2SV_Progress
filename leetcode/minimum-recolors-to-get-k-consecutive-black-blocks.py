class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[0:k]
        count = Counter(window)
        mini = count['W']
        for i in range(len(blocks)-k):
            
            if blocks[i] == 'W':
                count['W'] -= 1
            if blocks[i+k] == 'W':
                count['W'] += 1
            mini = min(mini,count['W'])
        return mini