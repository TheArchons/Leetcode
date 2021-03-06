class Solution:
    def twoSum(self, candidates, target):
        res = []
        for iPos, i in enumerate(candidates):
            for jPos, j in enumerate(candidates[iPos+1:]):
                if i + j == target:
                    res.append([i, j])
        return res

    def combinationSum2(self, candidates, target):
        if len(candidates) == 0:
            return []
        candidates = sorted(candidates)
        res = []
        for pos, i in enumerate(reversed(candidates)):
            visited = set()
            visited.add(len(candidates)-pos)
            curr = [i]
            depth = 0
            currPos = [pos]
            if i > target:
                continue
            while True:
                action = False
                for jPos, j in enumerate(candidates[:len(candidates)-pos-1]):
                    if jPos in visited or jPos in currPos:
                        continue
                    if sum(curr) + j == target:
                        res.append(sorted(curr + [j]))
                    elif sum(curr) + j < target:
                        curr.append(j)
                        currPos.append(jPos)
                        #visited.add(jPos)
                        depth += 1
                        action = True
                        continue
                    #backtrack
                    visited.add(jPos)
                    action = True
                    if len(curr) != 0:
                        curr.pop()
                        currPos.pop()
                    else:
                        action = False
                    depth -= 1
                    
                    break
                if not action:
                    break
        for i in self.twoSum(candidates, target):
            res.append(i)
        if target in candidates:
            res.append([target])

        #remove duplicates
        res = sorted(list(set(tuple(i) for i in res)))
        #convert to list
        res = [list(i) for i in res]
        return res


candidates = input().strip('[]').split(',')
for i in range(len(candidates)):
    candidates[i] = int(candidates[i])
target = int(input())
print(Solution().combinationSum2(candidates, target))