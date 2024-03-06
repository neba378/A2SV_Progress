class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        c = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if s[i-1] == '(':
                    ans+=(2**(len(stack)-1))
                stack.pop()
        return ans