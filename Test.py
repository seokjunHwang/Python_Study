# 복습
# 조건부 표현식 이해

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)  # zip 객체를 생성합니다.
# # zipped_list = list(zipped)  # zip 객체를 리스트로 변환합니다.
# print(zipped) # 출력 : <zip object at 0x1018ba300>
# print(*max(zipped),sep='\n')
# # print(zipped_list)  # 출력: [(1, 'a'), (2, 'b'), (3, 'c')]

print(*max((int(input()), i+1) for i in range(9)))

