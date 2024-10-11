class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        events = []
        
        for i in range(n):
            arrival, departure = times[i]
            events.append((arrival, departure, i))
        
        events.sort(key=lambda x: x[0])
        
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)
        
        occupied_chairs = []
        
        for arrival, departure, guest in events:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, freed_chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, freed_chair)
            
            assigned_chair = heapq.heappop(available_chairs)
            
            if guest == targetFriend:
                return assigned_chair
            
            heapq.heappush(occupied_chairs, (departure, assigned_chair))
        return -1