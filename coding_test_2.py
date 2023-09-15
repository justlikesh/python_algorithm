#2
### 2. 문제 설명

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# - "()()" 또는 "(())()" 는 올바른 괄호입니다.
# - ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# ### 제한사항

# - 문자열 s의 길이 : 100,000 이하의 자연수
# - 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
# 1. 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.

def solution3(s):
    answer = True
    stack = []
    
    for item in s:
        if stack and stack[-1] != item:
            if(stack[-1] == ")"):
                return False
            else:
                stack.pop()
        else:
            stack.append(item)
        
    
    if(stack):
        answer = False
        
    return answer

print(solution3("()()"))   
print(solution3("(())()")) 
print(solution3(")()("))   
print(solution3("(()("))   
print(solution3("(())))")) 
print(solution3(")")) 
print(solution3("())(()")) 