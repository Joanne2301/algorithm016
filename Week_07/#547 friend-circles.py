class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        Upper = [i for i in range(len(M))]

        def find(x):
            if Upper[x] != x: Upper[x] = find(Upper[x])
            return Upper[x]

        def union(x, y):
            Upper[find(y)] = find(x)
            return find(y)

        for x in range(len(M)):
            for y in range(x):
                if M[x][y]: union(x, y)
        for i in range(len(M)): find(i)
        return len(set(Upper))