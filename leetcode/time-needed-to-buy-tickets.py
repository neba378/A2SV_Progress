class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        queue = deque(list(range(0,len(t))))
        sec = 0
        while t[k]!=0:
            popped = queue.popleft()
            t[popped]-=1
            sec+=1
            if t[popped]!=0:
                queue.append(popped)
        return sec
