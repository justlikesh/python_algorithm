class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Let's find Exact Factorial
        fact = 1
        for i in range(1, n+1): 
            fact = fact * i
        
        # Conversion of a Number into String is limited by No. of Digits
        # So increasing the Limit
        sys.set_int_max_str_digits(100000)

        l = list(str(fact)) # Converting the Factorial digits into List 
        # print('l ',l) # Output Limit Exceeded

        ans = 0
        # Traversing through the List in Reverse 
        for i in range(len(l)-1, -1, -1):  
            if l[i] == '0':
                ans += 1

            if l[i] != '0':
                break

        return ans