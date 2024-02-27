class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = str(num)
        lst = []
        if num>=0:
            for i in nums:
                lst.append(i)
            
            lst.sort()
            i = 0
            while i<len(lst)-1 and lst[i] == "0":
                i+=1
            lst[i],lst[0] = lst[0],lst[i]
            s = "".join(lst)
            return int(s)
        else:
            for i in nums[1:]:
                lst.append(i)
            lst.sort(reverse=True)
            s = "".join(lst)
            return 0-int(s)