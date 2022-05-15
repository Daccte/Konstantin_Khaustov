import sys
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11, 45,
       73, 73, 46, 45, 98, 98, 99, 99, 101, 101, 2, 2, 7, 7, 45, 77, 111]
# result = []

result_1 = [src[i] for i in range(len(src)) if src.count(src[i]) == 1]
print(result_1, sys.getsizeof(result_1), perf_counter())

# for i in range(len(src)):
#     if src.count(src[i]) == 1:
#         result.append(src[i])

# print(result, sys.getsizeof(result), perf_counter())
