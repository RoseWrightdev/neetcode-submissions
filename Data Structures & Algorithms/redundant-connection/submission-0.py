class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        
        def dfs(node, parent):
            if node in visit:
                return True
            visit.add(node)
            for edge in adj[node]:
                if edge == parent:
                    continue
                if dfs(edge, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()
            if dfs(u, -1):
                return [u, v]
        return []

