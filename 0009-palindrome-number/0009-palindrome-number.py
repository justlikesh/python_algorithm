class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)
        mid = length // 2
        even = True if length % 2 == 0 else False
        
        if length == 1:
            return True
        
        if even:
            start = mid-1
        else:
            start = mid
        
        if x[:mid] == x[:start:-1]:
            return True
        
        else:
            False