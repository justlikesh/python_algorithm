class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0" # Just 0

        # Prepare negative sign & convert all values into absolute value
        negSign = "" if ((numerator < 0) == (denominator < 0)) else "-"
        numerator, denominator = abs(numerator), abs(denominator)

        # Determine the integer value, store decimals, and their indices
        intValue = str(numerator // denominator)
        remainderIndex, startIndex, lastIndex, decimals, repeating = {}, 0, 0, [], False

        # Answer without any decimal
        if numerator % denominator == 0:
            return negSign + intValue
        
        # Answer with decimal(s)
        while True:

            # Division operation
            decimals.append(numerator // denominator)
            remainder = numerator % denominator
            numerator = remainder * 10

            # Non-repeating answer
            if remainder == 0:
                repeating = False
                break
            
            # Repeating answer
            if remainder in remainderIndex:
                repeating = True
                startIndex = remainderIndex[remainder]
                break

            # Store remainder's index in operation
            remainderIndex[remainder] = lastIndex
            lastIndex += 1

        # Convert decimals into string
        decimals = ''.join(list(map(str, decimals[1:])))

        # Non-repeating answer
        if not repeating:    
            return negSign + intValue + "." + decimals

        # Repeating answer
        non_repeating_part = decimals[:startIndex]
        repeating_part = decimals[startIndex:lastIndex]
        return negSign + intValue + "." + non_repeating_part + f"({repeating_part})"