class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        prefix = [code[0]]
        for i in range(1,len(code)):
            prefix.append(code[i]+prefix[-1])
        ans = [0]*len(code)
        s = sum(code)
        if k == 0:
            return [0]*len(code)
        elif k>0:
            for i in range(len(code)):
                if i+k>=len(code):
                    ans[i] = prefix[(i+k)%len(code)]+s-prefix[i]
                
                else:
                    ans[i] = prefix[i+k]-prefix[i]
    

        else:
            for i in range(len(code)):
                if i == 0:
                    ans[i] = s-prefix[len(code)+k-1]
                elif i+k<0:
                    p = -(k+i)
                    ans[i] = s-prefix[len(code)-p-1]+prefix[i-1]
                elif i == -k:
                    ans[i] = prefix[i-1]
                else:
                    ans[i] = prefix[i-1] - prefix[i+k-1]
        return ans
