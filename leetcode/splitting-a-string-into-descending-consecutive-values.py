class Solution:
    def splitString(self, s: str) -> bool:
        def back(ind,curr):
            if ind == len(s):
                return len(curr)>=2
            for i in range(ind,len(s)+1):
                num = int(s[ind:i+1])
                print(num)
                if not curr or curr[-1] - 1 == num:
                    curr.append(num)
                    ans = back(i+1,curr)
                    curr.pop()
                    if ans:
                        return True
                if curr and num>=curr[-1]:
                    return False
            return False
        return back(0,[])


            
                
