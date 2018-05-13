def next_states(state):
    res = []
    for i, ch in enumerate(state):
        num = int(ch)
        res.append(state[:i] + str((num - 1) % 10) + state[i+1:])
        res.append(state[:i] + str((num + 1) % 10) + state[i+1:])
    return res


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        terminals = set(deadends)
        if '0000' in terminals:
            return -1
        terminals.add('0000')
        level, depth = {'0000'}, 0
        while level:
            if target in level:
                return depth
            level = {ns for state in level for ns in next_states(state) if ns not in terminals}
            terminals.update(level)
            depth += 1
        return -1