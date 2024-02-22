class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack and stack[-1] == d[i]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        
        
        
        
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif stack or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0