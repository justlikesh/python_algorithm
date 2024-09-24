class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        def bfs(i, j):
            if i >= rows or j >= cols:
                return 0
            if (i, j) not in cache:
                down = bfs(i + 1, j)
                diag = bfs(i + 1, j + 1)
                right = bfs(i, j + 1)
                cache[(i, j)] = 0
                if matrix[i][j] == '1':
                    cache[(i, j)] = 1 + min(down, diag, right)
            return cache[(i, j)]
        bfs(0, 0)
        max_len = max(cache.values(), default=0)
        return max_len ** 2