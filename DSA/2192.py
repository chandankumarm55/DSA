'''
Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

step 1 : create a 2d array of res to store te result and graph array for storing thr bidirectional matrix

step 2 : find the adjancency list and sotre it in graph array
graph = [[3, 4], [3], [4, 7], [5, 6, 7], [6], [], [], []]

step 3 : call the dfs search calling recursively and storing the result in res and not visiting the visited node

        def dfs(start , node , visited):
            for neighbour in graph[node]:
                if neighbour not in visited:
                    res[neighbour].append(start)
                    visited.add(neighbour)
                    dfs(start , neighbour , visited)
res = [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

step 4 : we need to sort the res array by how many elelemt are present in the each node 
     for i in range(n):
            res[i].sort()
final result is : [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
'''
class Solution(object):
    def getAncestors(self, n, edges):
        res = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]
        
        # Build the adjacency list
        for edge in edges:
            graph[edge[0]].append(edge[1])
        

        def dfs(start , node , visited):
            for neighbour in graph[node]:
                if neighbour not in visited:
                    res[neighbour].append(start)
                    visited.add(neighbour)
                    dfs(start , neighbour , visited)

        for i in range(n):
            visited = set()
            dfs(i , i , visited)
        
        # Sort each list of ancestors
        for i in range(n):
            res[i].sort()
        
        return res
    
solution = Solution()
n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
ans = solution.getAncestors(n, edgeList)
print(ans)
