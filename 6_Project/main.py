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

# def parse(s,i):
#     arr = ''
#     real = s[:i]
#     count = 1
#     for j in range(1, len(s)//i+2):
#         if real == s[i*j:i*(j+1)]:
#             count += 1
#         else:
#             real = (str(count) if count > 1 else '') + real
#             arr += str(real)
#             count = 1
#             real = s[i*j:i*(j+1)]
#     return len(arr)
#
# def solution(s):
#     dic = []
#     if len(s) == 1:
#         return 1
#     for i in range(1, len(s)//2+1):
#         dic.append(parse(s,i))
#     return min(dic)

# 최후의 문제 10번
# def tilt(s):
#     length = len(s)
#     answer = [[0 for i in range(length)] for j in range(length)]
#
#     for i in range(length):
#         for j in range(length):
#             answer[j][length-1-i] = s[i][j]
#     return answer
#
# def check(total, keyLength, length):
#     for i in range(keyLength-1, length-keyLength+1):
#         for j in range(keyLength-1, length-keyLength+1):
#             if total[i][j] in [0,2]:
#                 return False
#
#     return True
#
# def insert(total,row,col,key):
#     for i in range(len(key)):
#         for j in range(len(key)):
#             total[row+i][col+j] += key[i][j]
#     return total
#
# def solution(key, lock):
#     keyLength = len(key)
#     lockLength = len(lock)
#     key2 = key
#
#     length = lockLength + 2 * (keyLength - 1)
#
#     total = [[0 for i in range(length)] for i in range(length)]
#
#     for i in range(keyLength-1, length-keyLength+1):
#         for j in range(keyLength-1, length-keyLength+1):
#             total[i][j] = lock[i-(keyLength-1)][j-(keyLength-1)]
#
#     for i in range(4):
#         key2 = tilt(key2)
#         for i in range(length-keyLength+1):
#             for j in range(length-keyLength+1):
#                 copy = [[i for i in j] for j in total]
#                 result = insert(copy, i, j, key2)
#                 if check(result,keyLength,length):
#                     return True
#
#     return False
#
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

#최후의 문제 11번
# def findTail(total):
#     return min([(total[i][j], i, j) for i in range(len(total)) for j in range(len(total)) if total[i][j] > 0])[1:]
#
# length = int(input())
# total = [[0 for i in range(length+2)] for j in range(length+2)]
#
# apples = int(input())
# for i in range(apples):
#     row,col = list(map(int,input().split(' ')))
#     total[row][col] = -1
# total[1][1] = 1
# turns = int(input())
# turnsInfo = ['X' for i in range(10001)]
# for i in range(turns):
#     time, to = list(input().split(' '))
#     turnsInfo[int(time)] = to
#
# timeCount = 0
#
# # 0,1 -> 1,0 -> 0,-1 -> -1,0
#
# tilArr = [[0,1],[1,0],[0,-1],[-1,0]]
# til = 0
# ################
# tail = [1,1]
# head = [1,1]
# ################
# while True:
#     if turnsInfo[timeCount] == 'D':
#         til = til+1 if til < 3 else 0
#     elif turnsInfo[timeCount] == 'L':
#         til = til-1 if til > 0 else 3
#
#     nextPositionRow = head[0]+tilArr[til][0]
#     nextPositionCol = head[1]+tilArr[til][1]
#
#     if total[nextPositionRow][nextPositionCol] >= 1:
#         print(timeCount+1)
#         break
#     if nextPositionRow in [0, length+1] or nextPositionCol in [0, length+1]:
#         print(timeCount+1)
#         break
#
#     if total[nextPositionRow][nextPositionCol] == -1:
#         total[nextPositionRow][nextPositionCol] = total[head[0]][head[1]]+1
#         head=[nextPositionRow, nextPositionCol]
#     else:
#         total[nextPositionRow][nextPositionCol] = total[head[0]][head[1]] + 1
#         total[tail[0]][tail[1]] = 0
#         head = [nextPositionRow, nextPositionCol]
#         tail = findTail(total)
#
#     timeCount += 1

# 최후의 문제 13번


