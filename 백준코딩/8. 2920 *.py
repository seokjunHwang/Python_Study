# https://www.acmicpc.net/problem/2920
# 문제 2024.01.31
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.
# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

# 처음에 if문으로 해보고 숏코딩해봄
num_list = list(map(int, input().split()))
print([['mixed','descending'][num_list == sorted(num_list, reverse = True)]
          ,'ascending'][num_list == sorted(num_list)])

# 다른 숏코딩1
a=input()[2::2]
print({a:'mixed','2345678':'ascending','7654321':'descending'}[a])

# 다른 숏코딩2
print({"2345678":"ascending","7654321":"descending"}.get(input()[2::2],"mixed"))

# get메서드로 딕셔너리의 주어진 키에 해당하는 값을 찾고, 만약 없다면 기본값(mixed 선택옵션)을 반환한다.
# [2::2]
# 인덱스2부터 끝까지 슬라이싱, 2칸씩 건너뛰며 요소추출
# get함수 : 주로 딕셔너리에 사용
# my_dict = {'name': 'Alice', 'age': 30}
# print(my_dict.get('name', 'Unknown'))  # 출력: Alice
# print(my_dict.get('gender', 'Unknown')) # 출력: Unknown

# 내용) 슬라이싱, get
# 인풋:12345678 [5:2:-1]이라면?
# '5'인덱스인 6부터 거꾸로 '2'인덱스인 3의 바로앞인자(4)까지 슬라이싱, -1이므로 거꾸로 1칸씩 건너뛰며 요소추출
# 출력 : 654

# 원본자체를 바꾸는 오름/내림차순 함수?
# num_list.sort() 오름, num_list.sort(reverse=True) 내림
