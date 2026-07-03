class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(node):
            if node in visit:
                return 0
            
            visit.add(node)
            for edge in adj[node]:
                dfs(edge)
            return 1
        conns = 0
        for node in range(n):
            conns += dfs(node)
        return conns