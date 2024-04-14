from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        alwaysSortingList = SortedList()
        tot_cost = 0
        for inst in instructions:
            cost_of_ins = min(alwaysSortingList.bisect_left(inst),len(alwaysSortingList)-alwaysSortingList.bisect_right(inst))
            tot_cost+=cost_of_ins
            alwaysSortingList.add(inst)
        return tot_cost%(1000000007)