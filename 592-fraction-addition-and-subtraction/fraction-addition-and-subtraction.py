class Solution:
    def fractionAddition(self, expression: str) -> str:
        lst = re.findall(r'[+-]?\d+/\d+', expression)
        lst2 = []  
        l =1
        for ex in lst:
            nu,de = ex.split("/")
            lst2.append([nu,de])
            l = math.lcm(int(de),l)
        tot = 0
        for nu,de in lst2:
            tot+=(int(nu)*l/int(de))
        nu= tot//math.gcd(int(tot),l)
        de = l//math.gcd(int(tot),l)
        
        return str(int(nu))+"/"+str(int(de))


       