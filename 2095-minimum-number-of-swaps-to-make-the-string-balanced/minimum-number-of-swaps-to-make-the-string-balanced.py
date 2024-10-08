class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        counter = 0
        for brack in s:
            if brack == "]":
                if stack:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        counter+=1
                        stack.append(brack)
                else:
                    counter+=1
                    stack.append(brack)
            else:
                stack.append(brack)

        return math.ceil(counter/2)