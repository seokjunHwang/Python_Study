# 복습
# 조건부 표현식 이해

a,b = map(int, input().split())
print(['><'[a<b],'='][a==b])

# 별찍기, 오른쪽정렬
n = int(input())
[print(('*'*(i+1)).rjust(n)) for i in range(n)]

# Comprehension 숏코딩
num=int(input())
[print(('*'*(i+1)).rjust(num)) for i in range(num)]

# 최소최대
n, num = int(input()), list(map(int,input().split()))
print(min(num),max(num))