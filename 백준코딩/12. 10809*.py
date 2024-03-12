# https://www.acmicpc.net/problem/10809

# 문제 : 앒파벳찾기
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
import string

letters = []
voka = input()
for i in string.ascii_lowercase:
    a = voka.find(i) # index(i)는 없을경우 error발생
    letters.append(a)
print(*letters)

# 숏코딩
voka = input()
print(*[voka.find(i) for i in string.ascii_lowercase])

# 다른 숏코딩 chr(유니코드 해당문자로 변환)
voka = input()
print(*[voka.find(chr(i)) for i in range(97,123)])

# 다른분 숏코딩 (이중 map)
print(*map(input().find,map(chr,range(97,123))))

# 내용
# 아스키,인덱스(find,index()),*,이중map

print(*map(input().find,map(chr,range(97,123))))
