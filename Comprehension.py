# List Comprehension Code practice

s = "hwangseokjun hahaha"

s_list = []
for i in range(0, len(s), 2):
    s_list.append(s[i:i+2])

# Comprehension Code
s_list = [s[i:i+2] for i in range(0, len(s), 2)]

# result : ['hw', 'an', 'gs', 'eo', 'kj', 'un', ' h', 'ah', 'ah', 'a']


# practice 2

a = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in a]
print(new_list)  

# result : [2, 4, 6, 8, 10]


