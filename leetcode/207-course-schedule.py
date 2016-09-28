from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        marked = set()

        def visit(course):
            if course in marked:
                return True
            marked.add(course)
            for other in graph[course]:
                cycle = visit(other)
                if cycle:
                    return True
            visited.add(course)
            marked.remove(course)

        for course in range(numCourses):
            if course in visited:
                continue
            cycle = visit(course)
            if cycle:
                return False

        return True


if __name__ == '__main__':
    f = Solution().canFinish

    assert f(2, [[0, 1]]) is True
    assert f(2, [[1, 0], [0, 1]]) is False
    assert f(3, [[0, 1], [0, 2]]) is True
    assert f(3, [[0, 1], [1, 2], [2, 0]]) is False
    assert f(3, [[1, 0], [2, 1]]) is True
