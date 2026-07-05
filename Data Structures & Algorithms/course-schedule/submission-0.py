from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            if not adj[node]:
                return True
            visit.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            adj[node] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
