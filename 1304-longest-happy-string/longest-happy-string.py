import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        heap = []
        for cnt, ch in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if cnt:
                heapq.heappush(heap, (cnt, ch))
        while heap:
            cnt, ch = heapq.heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == ch:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                ans += ch2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(heap, (cnt2, ch2))
            else:
                ans += ch
                cnt += 1
            if cnt:
                heapq.heappush(heap, (cnt, ch))
        return ans
