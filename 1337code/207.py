class Solution:
    def canFinish(self, numCourses, prerequisites) :
        def hasLoop(curr, numCourses, prerequisites, visited):
            if visited[curr] == 1:
                return True

            if visited[curr] == 2:
                return False
            
            visited[curr] = 1

            for prereq in prerequisites[curr]:
                if hasLoop(prereq, numCourses, prerequisites, visited):
                    return True
            
            visited[curr] = 2
            return False
            
            
        graph = [[] for i in range(numCourses)]
        
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        print(graph)
        visited = {}
        for i in range(numCourses):
            visited[i] = 0
        for i in range(numCourses):
            if visited[i] == 0:
                if hasLoop(i, numCourses, graph, visited):
                    return False
        
        return True

sol = Solution()
print(sol.canFinish(2, [[1,0],[0,1]]))