# DFS-1

## Problem1 (https://leetcode.com/problems/flood-fill/)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image == None or len(image) == 0 or image[sr][sc] == color :
            return image

        self.dirs = [[-1,0],[1,0],[0,-1],[0,1]] # U D L R
        self.m = len(image)
        self.n = len(image[0])
        self.oldColor = image[sr][sc]
        self.dfs(image , sr, sc, color)
        return image


    def dfs(self, image: List[List[int]], row: int, col: int, color: int) -> None:
        #base
        if row < 0 or row >= self.m or col < 0 or col >= self.n or image[row][col] != self.oldColor :
            return

        #logic
        image[row][col] = color
        for Dir in self.dirs:
            nr = row + Dir[0]
            nc = col + Dir[1]
            self.dfs(image, nr, nc, color)
# TC = O(m*n) , SC = O(m*n)

## Problem2 (https://leetcode.com/problems/01-matrix/)

from queue import Queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat == None or len(mat) == 0:
            return []

        q = Queue()
        m = len(mat)
        n = len(mat[0])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]] # U D L R
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.put([i,j])
                elif mat[i][j] == 1:
                    mat[i][j] = -1

        lvl = 0
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                for Dir in dirs:
                    nr = curr[0] + Dir[0]
                    nc = curr[1] + Dir[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1:
                        q.put([nr , nc])
                        mat[nr][nc] = lvl + 1

            lvl = lvl + 1

        return mat
# TC = O(m*n), SC = O(m*n)        