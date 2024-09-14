class Solution:
    def defangIPaddr(self, address: str) -> str:
        lst = []
        for i in address:
            if i == ".":
                lst.append('[.]')
            else:
                lst.append(i)
        return "".join(lst)