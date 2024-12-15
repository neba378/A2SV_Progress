class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculateGain(passes,total):
            return ((passes+1)/(total+1))-passes/total
        maxHeap = []

        for nums in classes:
            heappush(maxHeap,[-calculateGain(nums[0],nums[1]),nums[0],nums[1]])
        for i in range(extraStudents):
            gain,passes,total = heappop(maxHeap)
            passes+=1
            total+=1
            newGain = calculateGain(passes,total)
            heappush(maxHeap,[-newGain,passes,total])
            
        count = 0
        for nums in maxHeap:
            count+=(nums[1]/nums[2])
        return (count)/len(classes)