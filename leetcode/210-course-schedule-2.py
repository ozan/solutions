from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        marked = set()
        topsort = []

        def visit(course):
            if course in marked:
                return True
            marked.add(course)
            for other in graph[course]:
                cycle = visit(other)
                if cycle:
                    return True
            if course not in visited:
                visited.add(course)
                topsort.append(course)
            marked.remove(course)

        for course in range(numCourses):
            if course in visited:
                continue
            cycle = visit(course)
            if cycle:
                return []

        return topsort


if __name__ == '__main__':
    f = Solution().canFinish

    assert f(2, [[0, 1]]) == [1, 0]
    assert f(2, [[1, 0], [0, 1]]) == []
    assert f(3, [[0, 1], [0, 2]]) == [2, 1, 0]
    assert f(3, [[0, 1], [1, 2], [2, 0]]) == []
    assert f(3, [[1, 0], [2, 1]]) == [0, 1, 2]
