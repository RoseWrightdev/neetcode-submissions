from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        completed, path = set(), set()
        result = []

        def dfs(node):
            if node in path:
                return False
            if node in completed:
                return True
            path.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            path.remove(node)
            completed.add(node)
            result.append(node)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        
        return result



