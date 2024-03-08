class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        tracking_dict = defaultdict(int)
        current_winner = persons[0]
        tracking_dict[current_winner] = 1
        self.winners_list = [current_winner]
        for i in range(1,len(self.persons)):
            tracking_dict[self.persons[i]]+=1
            if tracking_dict[self.persons[i]]>=tracking_dict[current_winner]:
                current_winner = self.persons[i]
            self.winners_list.append(current_winner)
            


    def q(self, t: int) -> int:
        x = bisect_right(self.times,t) - 1
        return self.winners_list[x]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)