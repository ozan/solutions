class Solution(object):
        
    def getImportance(self, employees, id):
        emps = {e.id: e for e in employees}
        def dfs(eid):
            return emps[eid].importance + sum(dfs(sub) for sub in emps[eid].subordinates)
        return dfs(id)