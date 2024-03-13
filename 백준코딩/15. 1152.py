# https://www.acmicpc.net/problem/1152
# 문제
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
# 입력
# 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
# 출력
# 첫째 줄에 단어의 개수를 출력한다.

stc = input().split(' ') # 이게 이미 리스트형태이다.

# 공백없애는 3가지
# 1. join
# 마지막 .split() 메서드가 문자열의 시작과 끝에 있는 공백을 자동으로 무시하기 때문에, 맨 앞과 맨 뒤의 공백은 최종 결과에 영향을 주지 않습니다.
# 중간에 긴공백도 다 없에준다.
stc = ' '.join(stc).split()
print(len(stc))

# 숏코딩 
print(len(' '.join(input().split(' ')).split()))

