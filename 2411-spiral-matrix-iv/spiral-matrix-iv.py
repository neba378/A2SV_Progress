# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        i, j = 0, 0
        direction = 0
        
        while head:
            matrix[i][j] = head.val
            head = head.next
            next_i = i + DIR[direction][0]
            next_j = j + DIR[direction][1]
            
            if not (top <= next_i <= bottom and left <= next_j <= right):
                if direction == 0:
                    top += 1
                elif direction == 1:
                    right -= 1
                elif direction == 2:
                    bottom -= 1
                elif direction == 3:
                    left += 1
                
                direction = (direction + 1) % 4
            
            i += DIR[direction][0]
            j += DIR[direction][1]
        
        return matrix
