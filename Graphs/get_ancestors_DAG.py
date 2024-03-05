# 2192

from collections import defaultdict
from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
        
        ans = []
        for i in range(n):
            queue = deque([i])
            visited = set()
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
            ans.append(sorted(list(visited)))
        
        return ans
