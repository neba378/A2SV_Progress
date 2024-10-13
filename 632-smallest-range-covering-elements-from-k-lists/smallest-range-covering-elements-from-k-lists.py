class Solution:
    def smallestRange(self, arrays: List[List[int]]) -> List[int]:
        pq = []
        max_val = float('-inf')
        
        for i in range(len(arrays)):
            heapq.heappush(pq, (arrays[i][0], i, 0))
            max_val = max(max_val, arrays[i][0])
        
        result = [-10**5, 10**5]
        
        while pq:
            min_val, arr_idx, el_idx = heapq.heappop(pq)
            
            if max_val - min_val < result[1] - result[0]:
                result = [min_val, max_val]
            
            if el_idx + 1 == len(arrays[arr_idx]):
                break
            
            next_val = arrays[arr_idx][el_idx + 1]
            heapq.heappush(pq, (next_val, arr_idx, el_idx + 1))
            
            max_val = max(max_val, next_val)
        
        return result
