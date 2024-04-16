# Definition for s

# Don't do anything...

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        head = ListNode(0)
        dummy = head
        
        while heap:
            _, idx, node = heapq.heappop(heap)
            head.next = node
            head = head.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
                
                
                
                