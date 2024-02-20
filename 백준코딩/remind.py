# # 2439 별찍기
# n = int(input())
# [print(('*'*i).rjust(n)) for i in range(1,n+1)]
# # for i in range(1, n+1):
# #     print(('*'*i).rjust(n))

# # 2675 텍스트 * 수 문장
# n = int(input())
# for _ in ra2nge(n):
#     num, text=  input().split(' ')
#     a = [i*int(num) for i in text]
#     print(''.join(a))

## 2884 알람시계
# h, m = map(int,input().split(' '))
# if m < 45:
#     print((h-1)%24, 60-(45 - m))
# else:
#     print(h,m - 45)
## 파이썬에서 음수 나머지연산 %
##  파이썬은 나머지가 항상 나눗수(여기서는 24)의 부호를 따르고 양수가 되도록 조정합니다.
## 따라서 -2%24이면 -2 = 24*-1 + 22로서, 몫이 -1이고 나머지가 22가된다.

# h, m = map(int, input().split(' '))
# print(h-(m<45)%24, (m-45)%60)

## 2920 음계
# a = list(input().split())
# if a == sorted(a):
#     print('ascending')
# elif a == sorted(a,reverse = True):
#     print('descending')
# else:
#     print('mixed')

## 숏코딩
# a = list(input().split())
# print( [['mixed','descending'][a == sorted(a, reverse=True)],'ascending']
#       [a == sorted(a)])

# 10250 ACM호텔
# 층은 나머지, 호수는 1+몫
n = int(input())
for _ in range(n):
    h, w, r = map(int, input().split())
    height = [r%h,h][r%h==0] * 100
    floor = [1+r//h,r//h][r%h==0]
    print(height+floor)

