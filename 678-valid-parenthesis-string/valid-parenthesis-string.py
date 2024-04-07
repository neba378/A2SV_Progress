class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        while stack and star:
            if stack[-1] > star[-1]:
                return False
            star.pop()
            stack.pop()
        return len(stack) == 0