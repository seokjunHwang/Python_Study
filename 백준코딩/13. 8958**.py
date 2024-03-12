# https://www.acmicpc.net/problem/8958
n = int(input())
for _ in range(n):
    a = input()
    X_index = 0
    score = 0 # 리스트사용하지 않고 변수생성하고하는게 시간복잡도가 더 작다.
    for i, char in enumerate(a,start=1):
        if char =='X':
            X_index = i
            continue # 다음인덱스로 넘어감
        next_X_index = i - X_index
        score += next_X_index
    print(sum(score))
            
# 내용
# enumerate(이터레이블,start=) : (인덱스, 요소) 튜플형식으로 순회하며 생성
# continue: 나머지아래코드건너뛰어서 다음반복문진행
# pass: 임시로 그자리를 채우는역할. 아래코드는 계속실행
# sum(이터레이블)


# 다른분 숏코딩
for i in[*open(0)][1:]:n=0
print(sum((n:=(n+1)*(j=='O'))for j in i))

# 할당 표현식(일명 "walrus operator") : 점수누적