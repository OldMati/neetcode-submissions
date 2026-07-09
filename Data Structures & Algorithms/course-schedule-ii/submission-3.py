class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {}    # all courses I need to take before course <key>
        for a, b in prerequisites:
            if a not in prereqs:
                prereqs[a] = []
            prereqs[a].append(b)

        visited = set()
        order = []

        def dfs(u):
            if u in visited:
                return
            visited.add(u)

            # search all children, then add u to order
            if u in prereqs:
                for v in prereqs[u]:
                    dfs(v)

            order.append(u)
        
        # build the topo order
        for u in range(numCourses):
            dfs(u)
        
        # there must be no cycle in the graph, checking it now; need to keep 2 sets: visited_before, visiting_now
        visited_before = set()
        visiting_now = set()
        # if visited the same node twice in one dfs, it means there is a cycle
        def has_cycle(u):
            if u in visited_before:
                return False     # no cycle here

            if u in visiting_now:
                print(f'Detected cycle at {u}')
                return True    # cycle here
            visiting_now.add(u)
            
            # explore all children; if any returns true, means there is a cycle
            if u in prereqs:
                for v in prereqs[u]:
                    print(f'has cycle; returning from vertex {u}')
                    if has_cycle(v):
                        return True
            visited_before.add(u)
            return False
            
        for u in range(numCourses):
            if has_cycle(u):
                return []
            visiting_now = set()
        
        return order


'''
represent the courses as a graph
the solution would be the topologically sorted graph
the graph must be acyclic (DAG)
for prerequisites[i] = [a, b], b must be taken before a, so the edge is from b to a; however, topological sort returns reversed order, so i will keep a -> b

'''
        