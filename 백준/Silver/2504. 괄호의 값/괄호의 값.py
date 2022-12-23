import sys
input = sys.stdin.readline
입력 = input
괄호 = 입력()
스택 = []
정답=0
곱=1
임시길이=len(괄호)
for 인덱스 in range(0,임시길이):
    if 괄호[인덱스] == '(':
        스택.append('(')
        곱=곱*2
    elif 괄호[인덱스] == '[':
        스택.append('[')
        곱=곱*3
    elif 괄호[인덱스] == ')':
        #에러
        if len(스택) ==0:
            정답=0
            break
        if 스택[-1] == '[':
            정답=0
            break
        if 괄호[인덱스-1] == '(':
            정답 = 정답 + 곱
        스택.pop()
        곱 = 곱//2
    elif 괄호[인덱스] == ']':
        #에러
        if len(스택) == 0:
            정답 = 0
            break
        if 스택[-1] =='(':
            정답=0
            break
        if 괄호[인덱스-1]=='[':
            정답 = 정답 + 곱
        곱 = 곱 // 3
        스택.pop()
if len(스택) != 0:
    정답=0
print(정답)
    
