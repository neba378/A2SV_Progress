class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
        seeker = 1
        placeholder = 0
        while(seeker<len(nums)):
            if nums[placeholder] != 0:
                placeholder+=1     
            else:
                if nums[seeker] != 0:
                    nums[placeholder] = nums[seeker]
                    nums[seeker] = 0
                    placeholder+=1
            seeker+=1

       
        