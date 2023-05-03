n = int(input())
l = list(map(int, input().split()))
d = [0] * n

l.sort()

d[0]= l[0]
sum = d[0]
for i in range(1, n):
    d[i] = d[i - 1] + l[i]
    sum = sum + d[i]
print(sum)

# for i in range(1, n):
#     insert_index = i
#     insert_value = l[i]
#
#     for j in range(i, -1, -1):
#         if l[j] < insert_value:
#             insert_index = j + 1
#             break
#
#         if j == 0:
#             insert_index = 0
#
#     for j in range(i, insert_index, -1):
#         l[j] = l[j - 1]
#     l[insert_index] = insert_value


# d[0]= l[0]
# for i in range(1, n):
#     d[i] = d[i - 1] + l[i]
#
# print(sum(d))
