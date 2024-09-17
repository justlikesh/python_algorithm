class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        def dfs(index,prev,total):
            if len(prev) ==k:
                if total==n:
                    ret.append(prev)
                return
            
            for i in range(index,10):           
                    curr=total+i
                    if curr<=n:
                        dfs(i+1,prev+[i],curr)
        dfs(1,[],0)
        return ret