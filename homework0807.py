#1 아래의 {해당 부분을 작성하세요} 부분을 첫번째 코드와 동일하게 동작하도록 작성하세요.
my_string = "nicebangtobangmeetbangyou"
def convert_split(string, target):
    split_array = my_string.split("bang")
    return split_array


print(convert_split(my_string, "bang"))

#2 아래의 {해당 부분을 작성하세요} 부분을 첫번째 코드와 동일하게 동작하도록 작성하세요.
investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
warning = "Kakao"


def check_warning_stock(list, warning):
    result = []
    for investment in investment_list:
        if investment != warning:
            result.append("투자 경고 종목이 아닙니다.")
        else:
            result.append("투자 경고 종목입니다.")
    
    return result 

print(check_warning_stock(investment_list,warning))

#3 아래의 {해당 부분을 작성하세요} 부분을 첫번째 코드와 동일하게 동작하도록 작성하세요.
important_number = ["821010-1635210", "921240-2635210","811122-4632215"]

def convent_number_to_gender(number_list):
    result = []
    for important in important_number:
        if int(important[7]) % 2 != 0:
            result.append('남자')
        else:
            result.append('여자')
    return result

print(convent_number_to_gender(important_number))

#4 아래의 {해당 부분을 작성하세요} 부분을 첫번째 코드와 동일하게 동작하도록 작성하세요.
number = [123, 456, 789]

def check_even_odd(number_list):
    result = []
    for num in number:
        if(num % 2 == 0):
            result.append("짝수")
        else:
            result.append("홀수")
    return result

print(check_even_odd(number))

#5 아래의 {해당 부분을 작성하세요} 부분을 첫번째 코드와 동일하게 동작하도록 작성하세요.
s = "2three45sixseven"
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}


def convert_alpha_to_number(string):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return answer
print(convert_alpha_to_number(s))


    



#1 숫자로 이루어진 문자열 `t`와 `p`가 주어질 때, `t`에서 `p`와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 `p`가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.
    
#    예를 들어, `t`="3141592"이고 `p`="271" 인 경우, `t`의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.


def solution1(t,p):
    t  = "3141592"
    p  = "271"

    t2 = "500220839878"
    p2 = "7"

    t3 = "10203" 
    p3 = "15"
    for num in t:
        print(num)

#2 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
n = 10
n1 = 12
x= ""

#if n % int(x) == 1 :
#    min(x)
#    print(x)

#3 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

absolutes = [4, 7, 12]
signs = ['True', 'False', 'True']


absolutes2 = [1,2,3]
signs2 = ['False','False','True']

def solution3(absolutes, signs):
    dap = []
    info = dict(zip(absolutes,signs))
    for num, sol in info.items():
        if sol == 'True':
            dap.append(num)
        else:
            dap.append(-num)
    return sum(dap)

print(solution3(absolutes,signs))
print(solution3(absolutes2,signs2))

#4 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
#  이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다.
#  즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
#  놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
#  단, 금액이 부족하지 않으면 0을 return 하세요.

price = 3
money = 20
count = 4
count2 = 3
count3 = 2
counts = (4,3,2)

#change = money - (price * n)
#for n in change:
#    print(n)



def solution4(price, money, counts):
    change=[]
    info = dict(zip(price, money, counts))
    for price, money, counts in info.items():
        if change <= money - (price * n):
            change.append(change)
        else:
            print(0)
    return sum(change)



print(solution4(price,money,counts))





