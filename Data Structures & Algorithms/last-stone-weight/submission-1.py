class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(stones)

        while len(heap) > 1:
            x, y = heapq.heappop_max(heap), heapq.heappop_max(heap)
            if y < x:
                heapq.heappush_max(heap, x - y)
        
        if not heap:
            return 0
        else:
            return heap[0]
