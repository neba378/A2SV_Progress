class Solution:
    def minSteps(self, number: int) -> int:
        fact, ans = 2, 0 
        maxi = int(math.sqrt(number))+1
        while fact <= maxi:
            while number%fact == 0: 
                ans += fact
                number = number//fact
            else: 
                fact += 1 if fact == 2 else 2
                
        if number > 2: 
            ans += number
            
        return ans