class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        count = 0
        for i,j in counter.items():
            count+=(i+j)//(i+1)*(i+1)
        print(counter)
        return count