class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = [i for i in part]
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>= len(part):
                if stack[len(stack)-len(part):] == part:
                    stack = stack[:len(stack)-len(part)]
        return "".join(stack)