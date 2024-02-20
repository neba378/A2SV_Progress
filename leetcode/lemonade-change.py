class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0,20:0}
        for i in bills:
            if i == 5:
                dic[5]+=1
            elif i == 10:
                if dic[5] == 0:
                    return False
                else:
                    dic[5]-=1
                    dic[10]+=1
            else:
                if dic[10]==0:
                    if dic[5]<3:
                        return False
                    else:
                        dic[5]-=3
                        dic[20]+=1
                else:
                    if dic[5]==0:
                        return False
                    else:
                        dic[10]-=1
                        dic[5]-=1
                        dic[20]+=1
        return True
            