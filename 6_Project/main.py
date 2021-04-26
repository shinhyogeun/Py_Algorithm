## 그리디 알고리즘

# 최후의 문제 1번
# length = int(input())
# arr = list(map(int,input().split()))
#
# sortedArr = sorted(arr, reverse=True)
#
# answer = 0
#
# while len(sortedArr) != 0:
#     king = sortedArr[0]
#
#     if len(sortedArr) >= king:
#         del sortedArr[:king]
#         answer = answer + 1
#         continue
#     break
#
# print(answer)


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

# length = int(input())
#
# arr = list(map(int,input().split(" ")))
# arr.sort()
#
# answer = 1
#
# for i in arr:
#     if i <= answer:
#         answer += i
#     else:
#         break
#
# print(answer)

# 최후의 문제 5번

# length, ran = map(int,input().split())
# arr = list(map(int,input().split(" ")))
#
# filterArr = set(arr)
#
# new = {}
#
# answer = (length * (length-1)) / 2
#
# for i in filterArr:
#     new[i] = arr.count(i)
#
# for key,value in new.items():
#     if value != 1:
#         answer -= (value * (value-1)) / 2
#
# print(int(answer))

# 최후의 문제 6번

## 별로인 방법
# def solution(food_times, k):
#     where = 0
#     count = 0
#
#     while count != k+1:
#         nowIndex = where % len(food_times)
#
#         if food_times[nowIndex] != 0:
#             if (count == k):
#                 return nowIndex+1
#             food_times[nowIndex] -= 1
#             count += 1
#             where += 1
#         else:
#             if(food_times.count(0) == len(food_times)):
#                 return -1
#             else:
#                 where += 1
#
# print(solution([3,1,2],5))

# import heapq
#
# def solution(food_times,k):
#     q = []
#     if sum(food_times) <= k:
#         return -1
#
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i+1))
#
#     minus = 0
#
#     while k >= (q[0][0]-minus) * len(q):
#         length = len(q)
#         new = heapq.heappop(q)[0]
#         good = (new-minus) * length
#         minus = new
#         k -= good
#
#     return sorted(q, key=lambda x:x[1])[k % len(q)][1]
#
# print(solution([2,3,1], 5))
# print(solution([4,3,5,6,2], 7))
# print(solution([3,1,1,1,2,4,3], 12))

# 구현 피지컬

# 최후의 문제 7번
# arr = list(map(int, input()))
#
# pivot = int(len(arr)/2)
#
# a = sum(arr[:pivot])
# b = sum(arr[pivot:])
# if(a == b):
#     print("LUCKEY")
# else:
#     print("READY")


# 최후의 문제 8번

# number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# arr = list(input())
#
# arr = sorted(arr)
#
# total = 0
# j = 0
#
# for i in range(len(arr)):
#     if arr[i-j] in number:
#         total += int(arr[i-j])
#         del arr[i-j]
#         j += 1
#     else:
#         break
#
# arr.append(str(total))
#
# print(''.join(arr))

# 최후의 문제 9번

def parse(s,i):
    arr = ''
    real = s[:i]
    count = 1
    for j in range(1, len(s)//i+2):
        if real == s[i*j:i*(j+1)]:
            count += 1
        else:
            real = (str(count) if count > 1 else '') + real
            arr += str(real)
            count = 1
            real = s[i*j:i*(j+1)]
    return len(arr)

def solution(s):
    dic = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        dic.append(parse(s,i))
    return min(dic)

print(solution("a"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

