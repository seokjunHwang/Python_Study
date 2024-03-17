# https://www.acmicpc.net/problem/2231
# 문제
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

# a = int(input())
# for i in str(a):
#     a += int(i)
# print(a)

# max(1,a) : 두수 중, 더 큰값출력
a = int(input())
l = []
for i in range(max(0,a-len(str(a))*9),a): 
    # max를 안써주면 1~8까지 i가 음수값이므로 밸류에러
    b = i
    for j in str(i):
        i += int(j)
    if i == a:
        l.append(b)
if l:
    print(min(l))
else:
    print(0)

# 다른 모범답안.
N = int(input())
ans = 0
for i in range(max(0,N-len(str(N))*9),N): # 
    if sum(map(int,str(i))) + i == N: 
        # 여기서 map을 쓰면 i문장 각각을 분해해서 하나씩 나열해주고, sum으로 모두 더한다
        ans = i
        break
print(ans)

# map 객체를 리스트로 변환하여 그 내용을 보여줄 수 있다!!
# map_object_list = list(map_object)