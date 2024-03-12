# 복습
# 조건부 표현식 이해

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)  # zip 객체를 생성합니다.
# # zipped_list = list(zipped)  # zip 객체를 리스트로 변환합니다.
# print(zipped) # 출력 : <zip object at 0x1018ba300>
# print(*max(zipped),sep='\n')
# # print(zipped_list)  # 출력: [(1, 'a'), (2, 'b'), (3, 'c')]


s = "qwxer"
reset_index = 0  # 'x' 이후부터 인덱스를 리셋하기 위한 변수

for i, char in enumerate(s):
    if char == 'x':  # 'x'를 만나면
        reset_index = i + 1  # 현재 인덱스 다음부터 리셋 시작
        continue # 건너뜀
    # 'x' 이후의 인덱스를 계산하기 위해 현재 인덱스에서 reset_index를 뺌
    current_index_after_reset = i - reset_index
    print(f"문자: {char}, 리셋된 인덱스: {current_index_after_reset}")

