def backtrack(n, leftCount, rightCount, output, result):
    # Base case where count of left and right braces is "n"
    if leftCount >= n and rightCount >= n:
        # Join the array elements into a string without any separators.
        outputStr = "".join(output)
        result.append(outputStr)

    # Case where we can still append left braces
    if leftCount < n:
        output.append("(")
        backtrack(n, leftCount + 1, rightCount, output, result)
        output.pop()

    # Case where we append right braces if the current count of right braces is less than the count of left braces
    if rightCount < leftCount:
        output.append(")")
        backtrack(n, leftCount, rightCount + 1, output, result)
        output.pop()


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        output = []
        backtrack(n, 0, 0, output, result)
        return result