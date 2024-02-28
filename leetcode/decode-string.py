class Solution:
    
    def decodeString(self, s: str) -> str:
            stack=[]
            for i in range(len(s)):
                if s[i]==']':
                    temp=[]
                    while stack and stack[-1]!='[':
                        temp.append(stack.pop())
                    stack.pop()
                    temp.reverse()
                    temp="".join(temp)
                    digit=[]
                    while  stack and  (stack[-1]).isdigit():
                        digit.append(stack.pop())
                    digit.reverse()
                    digit=int("".join(digit))
                    val=digit*temp
                    stack.append(val)
                else:
                    stack.append(s[i])
            return "".join(stack)
        

