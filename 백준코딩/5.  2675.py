# https://www.acmicpc.net/problem/2675

# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
# 2
# 3 ABC
# 5 /HTP
# 출력
# 각 테스트 케이스에 대해 P를 출력한다.
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

# 내 답
n = int(input())
for _ in range(n):
    num, text = input().split(' ',1)
    a = [i*int(num) for i in text]
    print(''.join(a))


# 정답
n = int(input())
for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김

# 설명
# 입력 예제 중, 특별한조건이 있으면 if문을 달아주면 된다.
# split(' ',1)에서 1은 최대분할횟수
# 컴프리헨션은 바로 리스트가 된다.
# join은 리스트의 특정인자로 나뉘어있는 요소들을 합쳐준다. 
# 백준 valueerror가 뜰 땐, 입력예제1를 넣었을 시, 출력1이 나오는지 확인해본다. 문제를 잘못이해했을수있다.