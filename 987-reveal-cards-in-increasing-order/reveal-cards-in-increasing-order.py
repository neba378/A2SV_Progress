class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        ans = [0]*len(deck)
        for card in deck:
            ind = queue.popleft()
            ans[ind] = card
            if queue:
                queue.append(queue.popleft())
        return ans