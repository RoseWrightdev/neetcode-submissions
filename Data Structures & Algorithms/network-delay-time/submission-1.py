class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        heap = [(0, k)]
        visit = set()
        time = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(heap, (w1 + w2, n2))
        return time if len(visit) == n else -1
            
