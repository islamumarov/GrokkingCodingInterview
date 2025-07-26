from collections import defaultdict, deque
from typing import List


class FindPath:
    def validPathDFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)

        def dfs(curr, graph):
            if curr == destination:
                return True
            for i in graph[curr]:
                if i not in seen:
                    seen.add(i)
                    if dfs(i,graph):
                        return True
            return False

        return dfs(source, graph)
    def validPathDFSWithStack(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        curr = source
        stack = [source]
        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            for i in graph[curr]:
                if i not in seen:
                    seen.add(i)
                    stack.append(i)

        return False
    def validPathBFSWithDeque(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        queue = deque()
        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for i in graph[curr]:
                if i not in seen:
                    seen.add(i)
                    queue.append(i)

        return False


if __name__ == '__main__':
    n = 10
    edges =[[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    source = 5
    destination = 9

    sol = FindPath()
    print(sol.validPathDFSWithStack(n, edges,source,destination))
