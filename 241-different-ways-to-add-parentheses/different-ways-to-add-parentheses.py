class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y
        }
        def bt(left,right):
            result = []
            for i in range(left,right+1):
                if expression[i] in ops:
                    lst1 = bt(left,i-1)
                    lst2 = bt(i+1,right)
                    for n1 in lst1:
                        for n2 in lst2:
                            result.append(ops[expression[i]](n1,n2))
            if result == []:
                result = [int(expression[left:right+1])]
            return result
        return bt(0,len(expression)-1)