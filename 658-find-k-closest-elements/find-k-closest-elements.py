class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            diff = abs(i-x)
            heap.append((diff,i))
        heapify(heap)
        # Pop the k smallest elements from the heap and store their values
        result = [heappop(heap)[1] for _ in range(k)]

        # Sort the result in ascending order and return it
        return sorted(result)
