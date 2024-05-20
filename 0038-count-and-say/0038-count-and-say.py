class Solution:
    def countAndSay(self, n: int) -> str:
        # base
        say = "1"

        for i in range(2, n + 1):
            temp = ""
            num = say[0]
            count = 1
            for i in range(1, len(say)):
                curr_num = say[i]
                if num == curr_num: # same digit
                    count += 1
                else:               # different digit
                    temp += str(count) + str(num)
                    num = curr_num
                    count = 1
            temp += str(count) + str(num)

            # update say
            say = temp

        return say
            