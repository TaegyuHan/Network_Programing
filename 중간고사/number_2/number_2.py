tmp_list = ['H', 'e', 'l', 'l', 'o', ' ', 'I', 'a', 'T']

# A
tmp_list[7] = 'o'
print(tmp_list)

# B
tmp_list.append("?")
print(tmp_list)

# C
print(len(tmp_list))

# D
print("".join(tmp_list))

# E
print(sorted(tmp_list, reverse=True))
