class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        for j in range(1,len(boxes)):
            if boxes[j] == "1":
                ans[0]+=(abs(0-j))
        # return ans
        pre,post = [0],[0]
        for num in boxes:
            pre.append(pre[-1]+int(num))
        for i in range(len(boxes)-1,-1,-1):
            post.append(post[-1]+int(boxes[i]))
        # print(pre,post)
        for i in range(1,len(ans)):
            ans[i] = ans[i-1]+pre[i]-post[-i-1]
        return ans