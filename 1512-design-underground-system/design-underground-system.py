class UndergroundSystem:

    def __init__(self):
        self.users = defaultdict(list)
        self.places = defaultdict(int)
        self.count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id].append((stationName,t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ti = self.users[id][-1][1]
        start = self.users[id][-1][0]
        start_end = (start,stationName)
        self.places[start_end]+=(t-ti)
        self.count[start_end]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start_end = (startStation,endStation)
        return self.places[start_end]/self.count[start_end]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)