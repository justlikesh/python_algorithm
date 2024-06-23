class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack=[]
        ans=[]
        def com2(ind,target):
            if target==0:
                ans.append(stack[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]<=target:
                    stack.append(candidates[i])
                    com2(i+1,target-candidates[i])
                    stack.pop()
                else:
                    break

        com2(0,target)
        return ans

        