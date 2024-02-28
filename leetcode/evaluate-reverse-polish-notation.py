class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = {'+','-','*','/'}
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y),"*": (lambda x,y: x*y),"/": (lambda x,y: x/y)}
        for i in tokens:
            if i in oper:
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(ops[i](x,y))
            else:
                stack.append(i)
        return int(stack[-1])