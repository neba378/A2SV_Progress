class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            st = i-1
            end = i+1
            count+=1
            # Odd
            while st>=0 and end<len(s):
                if s[st] == s[end]:
                    count+=1
                    st-=1
                    end+=1
                else:
                    break
            # Even
            if i!= len(s)-1:
                l,r = i,i+1
                while l>=0 and r<len(s):
                    if s[l] == s[r]:
                        count+=1
                        l-=1
                        r+=1
                    else:
                        break
        return count