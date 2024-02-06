# https://www.acmicpc.net/problem/2439

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 결과 :  '출력형식이 잘못되었습니다.' : range()부분
# 피드백 : range는 0부터시작하므로 아래코드는 별이 0개부터 5개까지 찍히게됨!! -> 오답
num = int(input())
for i in range(num+1):
    text = ('*'*i).rjust(num)
    print(text)

# 정답1
num = int(input())
for i in range(num):
    text = ('*'*(i+1)).rjust(num)
    print(text)

# Comprehension 숏코딩
num=int(input())
[print(('*'*(i+1)).rjust(num)) for i in range(num)]

# 정답2
i,num = 0,int(input())
while num-i: i+=1; print(f"{'*'*i:>{num}}")




# 위치정렬함수
# 오른쪽 정렬 : .rjust(n) 
# 가운데 정렬 : .center(n)
# 왼쪽 정렬  : .ljust(n)
# 여기서 n은 텍스트의 '총 길이'를 뜻하므로, 
# 예를들어,텍스트가 '1'이고 n을 5로 주면, '    1' 이렇게 왼쪽공백을 4로줘서 총 5로 맞춰준다.

# while문과 세미콜론 ;
# 세미콜론은 여러줄을 한 줄로 표현할때 사용
# while n-i 구문에 대해서는, 이는 while n-i != 0와 동일합니다. --> n-i 가 0이 아닐때(참일때) 루프를 계속돌아라
# 파이썬에서 0은 거짓(False)으로 평가되고, 0이 아닌 모든 값은 참(True)으로 평가됩니다. 
# 따라서 n-i가 0이 되면, while 루프의 조건이 거짓이 되어 루프가 종료됩니다. 
# while n-i == 0:라고 쓰는 것은 n-i가 0일 때 루프를 실행하라는 의미가 되므로, 의도한 바와는 다른 결과를 초래할 것입니다.
