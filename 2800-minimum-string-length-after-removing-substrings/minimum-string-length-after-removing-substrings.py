class Solution:
    def minLength(self, s: str) -> int:
        # if len(s)==1:
        #     return 1
        stack = [s[0]]
        for i in range(1,len(s)):
            stack.append(s[i])
            if len(stack)>1 and (stack[-1] == "B" and stack[-2] == "A" or stack[-1] == "D" and stack[-2] == "C"):
                stack.pop()
                stack.pop()
        return len(stack)
            
            
            
        