# 5. 10818 최대,최소값
# n = int(input())
# num = list(map(int, input().split()))
# print(min(num),max(num))

# 6. 2675 문자열반복
n = int(input())
for _ in range(n): # 범위 range 잊지말기!
    num, text = input().split()
    print(''.join([ i*int(num )for i in text]))