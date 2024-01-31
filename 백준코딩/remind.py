# 5. 2675문자열반복

n = int(input())
for _ in range(n):
    num, text = input().split()
    # print(''.join([i*int(num) for i in text]))
    [print(i*int(num),end='') for i in text]
    print()

# 7. 2844 알람시계
h,m = map(int,input().split())
print(h-(m<45)%24, (m-45)%60)

# 8. 2920 음계
print({'12345678':'ascending','87654321':'descending'}.get(input()[::2], 'mixed'))

