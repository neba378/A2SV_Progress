class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0]*(4*self.n)
        self.build(0,0,(self.n)-1)

    def getChildren(self,node):
        return 2*node+1,2*node+2
    def build(self,node,left,right):
        if left == right:
            self.tree[node] = self.nums[left]
            return
        l,r = self.getChildren(node)
        mid = (left+right)//2
        self.build(l,left,mid)
        self.build(r,mid+1,right)

        self.tree[node] = self.tree[l]+self.tree[r]
    def update1(self,node,left,right,index,value):
        if left == right:
            self.tree[node] = value
            self.nums[index] = value
            return
        mid = (left+right)//2
        l,r = self.getChildren(node)
        if index<=mid:
            self.update1(l,left,mid,index,value)
        else:
            self.update1(r,mid+1,right,index,value)
        self.tree[node] = self.tree[l]+self.tree[r]

    def update(self, index: int, val: int) -> None:
        self.update1(0,0,self.n-1,index,val)

    def sumRange(self, left: int, right: int) -> int:
        def sumy(node,l,r,lef,righ):
            if lef>righ:
                return 0
            if l == lef and r == righ:
                return self.tree[node]
            mid = (l+r)//2
            left,right = self.getChildren(node)
            left_sum = sumy(left,l,mid,lef,min(righ,mid))
            right_sum = sumy(right,mid+1,r,max(lef,mid+1),righ)
            return left_sum+right_sum 
        return sumy(0,0,self.n-1,left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)