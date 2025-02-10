class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        dig = '1234567890'
        for ch in s:
            if ch in dig:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)