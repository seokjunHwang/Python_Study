# https://www.acmicpc.net/problem/1157
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 1. 대문자로 바꾸고 -> 중복제거set -> 딕셔너리(요소,갯수) -> 갯수max얘들의 key들을 list -> 출력
# 2. set필요없다 : 어차피 딕셔너리는 키중복이 안되므로 set설정할필요가없다.
# 3. list필요없다 : 처음 sentence문장으로 받아와도 for문돌리면 알아서 해체되므로 
import time

sentence = list(input().upper())
start = time.time()  # 시작 시간 저장
dic = {}
for i in set(sentence):
    dic[i] = sentence.count(i)
max_keys = [key for key,value in dic.items() if value == max(dic.values())]
if len(max_keys) == 1 :
    print(max_keys[0])
else:
    print("?")

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간






