class Solution(object):
    def multiply(self, num1, num2):
        res1 = 0
        res2 = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num1)):
            res1 += (ord(num1[i]) - 48) * (10 ** i)
        
        for j in range(len(num2)):
            res2 += (ord(num2[j]) - 48) * (10 ** j)
        
        result = res1 * res2 
        
        sol = ""
        while result > 0:
            digit = result % 10
            sol += chr(digit + 48) 
            result //= 10
        if not sol:
            return "0"

        return sol[::-1]