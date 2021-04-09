class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class UF:
            def __init__(self, sz):
                self.parent = [i for i in range(sz)]
                self.sz = [1 for i in range(sz)]  # sz to keep the tree balanced

            def root(self, i):
                while self.parent[i] != i:
                    self.parent[i] = self.parent[self.parent[i]]  # path compression here
                    i = self.parent[i]

                return i

            def find(self, i):
                return self.root(i)

            def connected(self, i, j):
                return self.root(i) == self.root(j)

            def union(self, i, j):
                pi = self.root(i)
                pj = self.root(j)

                if pi == pj:
                    return

                if self.sz[pi] < self.sz[pj]:  # keeps size balanced
                    self.parent[pi] = pj
                    self.sz[pj] += self.sz[pi]
                else:
                    self.parent[pj] = pi  # keeps size balanced
                    self.sz[pi] += self.sz[pj]

        def cell_to_index(i, j):
            return i * C + j

        R, C = len(heights), len(heights[0])

        edges = []
        for r in range(R):
            for c in range(C):
                for n1, n2 in [(1, 0), (0, 1)]:
                    x = r + n1
                    y = c + n2
                    if x < R and y < C:
                        weight = abs(heights[x][y] - heights[r][c])
                        edges.append((weight, cell_to_index(r, c), cell_to_index(x, y)))

        edges = sorted(edges)
        uf = UF(R * C)

        for edge in edges:
            cost, source, dest = edge
            uf.union(source, dest)
            if uf.connected(cell_to_index(0, 0), cell_to_index(R - 1, C - 1)):
                return cost

        return 0