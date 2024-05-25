class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        def generate_gray_code(n):
            if n == 1:
                return [0, 1]
            
            smaller_gray_code = generate_gray_code(n - 1)
            mask = 1 << (n - 1)
            return smaller_gray_code + [x | mask for x in reversed(smaller_gray_code)]
        
        return generate_gray_code(n)

        