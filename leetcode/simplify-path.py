class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split("/")
        for i in lst:
            if len(i)>0:
                if i == "..":
                    if stack:
                        stack.pop()
                    else:
                        continue
                elif i =="":
                    continue
                elif i == ".":
                    continue
                else:
                    stack.append(i)

        answer = ""
        if len(stack) == 0:
            return "/"
        else:
            for i in stack:
                answer+="/"
                answer+=i
        return(answer)
                
        