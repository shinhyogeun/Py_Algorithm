## 그리디 알고리즘

# 최후의 문제 1번
length = int(input())
arr = list(map(int,input().split()))

sortedArr = sorted(arr, reverse=True)

answer = 0

while len(sortedArr) != 0:
    king = sortedArr[0]

    if len(sortedArr) >= king:
        del sortedArr[:king]
        answer = answer + 1
        continue
    break

print(answer)


# 최후의 문제 2번

# arr = list(map(int,list(input())))
# arr.insert(0,0)
#
# answer = 0
#
# for i in range(len(arr)-1):
#     if (arr[i] in [0,1] or arr[i+1] in [0,1]):
#         answer = answer + arr[i+1]
#     else:
#         answer = answer * arr[i+1]
#
# print(answer)

# 최후의 문제 3번

# arr = list(map(int,list(input())))
#
# a = 0
# b = 0
# pivot = 2
#
# for i in arr:
#     if(pivot != i):
#         pivot = i
#         if(i == 0):
#             a += 1
#         else:
#             b += 1
# print(a if a < b else b)


# 최후의 문제 4번

