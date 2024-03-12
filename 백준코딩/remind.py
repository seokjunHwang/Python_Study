# 2564

# l = []
# for _ in range(9):
#     num = int(input())
#     l.append(num)
# print(f"{max(l)}\n{1+l.index(max(l))}")
    

# 8958
n = int(input())
p = 0
q = 0
for _ in range(n):
    text = input()
    for i in text:
        if i == "X":
            p = 0
        else:
            p += 1
            q += p
    print(q)


