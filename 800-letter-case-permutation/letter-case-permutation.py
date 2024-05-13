class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        lst = [i for i in s]
        def rec(ind,st):
            ans.add("".join(st))
            for i in range(ind,len(lst)):
                try:
                    c = int(lst[i])
                except:
                    if st[i].islower():
                        st[i] = st[i].upper()
                    else:
                        st[i] = st[i].lower()
                    if "".join(st) not in ans:
                        rec(i+1,st)
                    if st[i].islower():
                        st[i] = st[i].upper()
                    else:
                        st[i] = st[i].lower()
        rec(0,lst)
        return(list(ans))
