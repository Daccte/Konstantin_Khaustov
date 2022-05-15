src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 45, 46, 47, 30, 199, 1000, 578, 847]

result = (src[i] for i in range(len(src)) if src[i] > src[i-1])
print(*result)

