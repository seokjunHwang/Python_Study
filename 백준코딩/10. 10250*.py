# https://www.acmicpc.net/problem/10250
# 입력
# 프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 
# 출력
# 프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

n = int(input())
a = list()
# 층 + 호수
for _ in range(n):
    h, w, custom = map(int, input().split())
    if custom%h == 0:
        a.append(h*100 + custom//h)
    else:
        a.append(custom%h*100 + (1+custom//h))

[print(i) for i in a]

# 바로바로 나와도되는거면
n = int(input())
for _ in range(n):
    h, w, custom = map(int, input().split())
    if custom%h == 0:
        print(h*100 + custom//h)
    else:
        print(custom%h*100 + (1+custom//h))

# 숏코딩 1
n = int(input())
for _ in range(n):
    h,_,c = map(int, input().split()) # 무의미한 입력값은 '_'으로 처리
    c -= 1                            # 순서, 수열관련은 인덱스를 0부터 시작하도록 맞추고 계산 후, 마지막에 +1로 조절하면 if문 필요없이 대부분의 경우의 수에 맞음
    print((c%h+1)*100 + c//h+1)

# 숏코딩 2
# for r in[*open(0)][1:]:h,_,n=map(int,r.split());n-=1;print((n%h+1)*100+n//h+1)
        

# 다른답안
# t = int(input())

# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n//h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n//h
#         floor = h
#     print(f'{floor*100+num}')


