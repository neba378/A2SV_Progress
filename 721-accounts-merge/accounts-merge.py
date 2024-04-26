class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)} # Using dictionary
        # self.parent = [i for i in range(size)] # Using list
        self.rank = defaultdict(int)
        
    def find(self, x):
        
        while(x != self.parent[x]):
            x = self.parent[x]
        return x
		
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if py!=px:
            if self.rank[py]>self.rank[px]:
                self.parent[px] = py
            elif self.rank[py]<self.rank[px]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px]+=1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        emailToID = {}
        n = 0
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in emailToID:
                    emailToName[email] = name
                    emailToID[email] = n
                    n += 1
        
        uf = UnionFind(n)
        
        for account in accounts:
            firstEmail = account[1]
            firstID = emailToID[firstEmail]
            for email in account[2:]:
                uf.union(firstID, emailToID[email])
        
        mergedAccounts = defaultdict(list)
        
        for email in emailToID:
            accountID = uf.find(emailToID[email])
            mergedAccounts[accountID].append(email)
        result = []
        
        for accountID in mergedAccounts:
            emails = mergedAccounts[accountID]
            name = emailToName[emails[0]]
            result.append([name] + sorted(emails))
        
        return result



















