# 9935번 폭발문자열
# from collections import deque
#
# arr = deque(input())
# bomb = list(input())
# answer = deque()
#
# while arr:
#     answer.append(arr.popleft())
#     if answer[-1] == bomb[-1] and len(answer) >= len(bomb):
#         for i in range(2,len(bomb)+1):
#             if answer[-i] != bomb[-i]:
#                 break
#         else:
#             for i in range(len(bomb)):
#                 answer.pop()
#
# if answer == deque():
#     print('FRULA')
# else:
#     print(''.join(answer))

#2407번 조합
# n,m = map(int,input().split())
# upper = 1
# under = 1
# for i in range(0,m):
#     upper *= n-i
# for i in range(2,m+1):
#     under *= i
# print(upper//under)

#1932번 정수삼각형
# n = int(input())
# arr = []
#
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
#
# for i in range(1,n):
#     for j in range(len(arr[i])):
#         if j == 0:
#             arr[i][0] += arr[i-1][0]
#         elif j == len(arr[i])-1:
#             arr[i][-1] += arr[i-1][-1]
#         else:
#             arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])
#
# print(max(arr[-1]))

#1629번 곱셈
# a,b,c = map(int,input().split())
#
# def poww(a,b,c):
#     if b == 1:
#         return a % c
#     if b%2 == 0:
#         return poww(a,b//2,c)**2 % c
#     else:
#         return poww(a,b//2,c)**2*poww(a,1,c) % c
#
# print(int(poww(a,b,c)))

#16953번 A -> B
# a,b = map(int,input().split())
# arr = []
# def goToNext(start,count):
#     if start >= b:
#         return
#     arr.append((start*2,count+1))
#     arr.append((int(str(start) + '1'),count+1))
#     goToNext(start*2,count+1)
#     goToNext(int(str(start)+'1'),count+1)
#
# goToNext(a,1)
#
# for i,n in arr:
#     if i == b:
#         print(n)
#         break
# else:
#     print(-1)

# 2096번 내려가기
# n = int(input())
# arr = [[i,i] for i in map(int,input().split())]
# maxi = 0
# mini = 1e9
#
# for i in range(n-1):
#     new = [[k,k] for k in map(int,input().split())]
#     for j in range(3):
#         if j == 0:
#             new[0][0] += max(arr[0][0], arr[1][0])
#             new[0][1] += min(arr[0][1], arr[1][1])
#         elif j == 2:
#             new[2][0] += max(arr[1][0], arr[2][0])
#             new[2][1] += min(arr[1][1], arr[2][1])
#         else:
#             new[1][0] += max(arr[0][0], arr[1][0], arr[2][0])
#             new[1][1] += min(arr[0][1], arr[1][1], arr[2][1])
#     arr = new
#
# for i in arr:
#     if i[0] > maxi:
#         maxi = i[0]
#     if i[1] < mini:
#         mini = i[1]
#
# print(maxi, mini)

# 12851번 숨바꼭질2
# from collections import deque
#
# INF = 1e9
#
# total = [[INF,1] for _ in range(100001)]
# start,end = map(int,input().split())
# total[start][0] = 0
# q = deque()
# q.append(start)
#
# while q:
#     now = q.popleft()
#     if 100000 >= now+1:
#         if total[now+1][0] > total[now][0] + 1:
#             total[now+1] = [total[now][0] + 1,1]
#             q.append(now + 1)
#         elif total[now+1][0] == total[now][0] + 1:
#             total[now+1][1] += 1
#             q.append(now + 1)
#     if now-1 >= 0:
#         if total[now-1][0] > total[now][0] + 1:
#             total[now-1] = [total[now][0] + 1, 1]
#             q.append(now - 1)
#         elif total[now-1][0] == total[now][0] + 1:
#             total[now-1][1] += 1
#             q.append(now - 1)
#     if 50000 >= now:
#         if total[now*2][0] > total[now][0] + 1:
#             total[now*2] = [total[now][0] + 1, 1]
#             q.append(now * 2)
#         elif total[now*2][0] == total[now][0] + 1:
#             total[now*2][1] += 1
#             q.append(now * 2)
# print(total[end][0])
# print(total[end][1])

# 1504번 특정한 최단 경로
# import heapq
#
# INF = 1e9
# n,m = map(int,input().split())
# dic = {i+1:[] for i in range(n)}
#
# for i in range(m):
#     frm,to,much = map(int,input().split())
#     dic[frm].append((much,to))
#     dic[to].append((much,frm))
#
# stop1,stop2 = map(int,input().split())
#
# def getMinimumDistance(frm,to):
#     xx = []
#     distance = [INF] * (n + 1)
#     heapq.heappush(xx, (0, frm))
#     distance[frm] = 0
#     while xx:
#         much,whr = heapq.heappop(xx)
#         if distance[whr] < much:
#             continue
#         for i in dic[whr]:
#             if much + i[0] < distance[i[1]]:
#                 distance[i[1]] = much + i[0]
#                 heapq.heappush(xx,(much + i[0],i[1]))
#     return distance[to]
# one = getMinimumDistance(1,stop1) + getMinimumDistance(stop1,stop2) + getMinimumDistance(stop2,n)
# two = getMinimumDistance(1,stop2) + getMinimumDistance(stop2,stop1) + getMinimumDistance(stop1,n)
#
# if one >= INF and two >= INF:
#     print(-1)
# else:
#     print(min(one,two))

# 1149번 RGB거리
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#
# for i in range(1,n):
#     for j in range(3):
#         if j == 0:
#             arr[i][j] += min(arr[i-1][j+1], arr[i-1][j+2])
#         if j == 1:
#             arr[i][j] += min(arr[i-1][j-1], arr[i-1][j+1])
#         if j == 2:
#             arr[i][j] += min(arr[i-1][j-1], arr[i-1][j-2])
#
# print(min(arr[-1]))

# 13549번 숨바꼭질3
# from collections import deque
#
# INF = int(1e9)
#
# total = [INF for i in range(100001)]
# start,end = map(int,input().split())
# total[start] = 0
# q = deque()
# q.append(start)
#
# while q:
#     now = q.popleft()
#     if 100000 >= now+1:
#         if total[now+1] > total[now] + 1:
#             total[now+1] = total[now] + 1
#             q.append(now+1)
#     if now-1 >= 0:
#         if total[now-1] > total[now] + 1:
#             total[now-1] = total[now] + 1
#             q.append(now-1)
#     if 50000 >= now:
#         if total[now*2] > total[now]:
#             total[now*2] = total[now]
#             q.append(now * 2)
#
# print(total[end])

# import heapq
# from collections import deque
#
# INF = 1e9
# n,m = map(int,input().split())
# dic = {i+1:[] for i in range(n)}
#
# for i in range(m):
#     frm,to,much = map(int,input().split())
#     dic[frm].append((much,to))
#     dic[to].append((much, frm))
#
# def getMinimumDistanceWhitQ(frm):
#     xx = deque()
#     distance = [INF] * (n + 1)
#     xx.append((0, frm))
#     distance[frm] = 0
#     count = 0
#     while xx:
#         count += 1
#         much,whr = xx.popleft()
#         if distance[whr] < much:
#             continue
#         for i in dic[whr]:
#             if much + i[0] < distance[i[1]]:
#                 distance[i[1]] = much + i[0]
#                 xx.append((much + i[0],i[1]))
#     return distance,count
#
# def getMinimumDistance(frm):
#     xx = []
#     distance = [INF] * (n + 1)
#     heapq.heappush(xx, (0, frm))
#     distance[frm] = 0
#     count = 0
#     while xx:
#         count += 1
#         much,whr = heapq.heappop(xx)
#         if distance[whr] < much:
#             continue
#         for i in dic[whr]:
#             if much + i[0] < distance[i[1]]:
#                 distance[i[1]] = much + i[0]
#                 heapq.heappush(xx,(much + i[0],i[1]))
#     return distance,count
#
# print(getMinimumDistance(1))
# print(getMinimumDistanceWhitQ(1))

# 9465번 스티커
# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# for i in range(n):
#     m = int(input())
#     arr = []
#     newArr = []
#
#     for i in range(2):
#         arr.append(list(map(int,input().split())))
#     for i in range(len(arr[0])):
#         newArr.append([arr[0][i],arr[1][i]])
#     if len(newArr) == 1:
#         print(max(newArr[0]))
#         break
#     newArr[1] = [newArr[1][0] + newArr[0][1],newArr[1][1]+newArr[0][0]]
#
#     for i in range(2,m):
#         newArr[i] = [newArr[i][0] + max(newArr[i-1][1],newArr[i-2][1]), newArr[i][1] + max(newArr[i-1][0], newArr[i-2][0])]
#
#     print(max(newArr[-1]))

# 11660번 구간 합 구하기
n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in arr:
    for j in range(1,len(i)):
        i[j] += i[j-1]
print(arr)
for i in range(1,len(arr)):
    new = []
    for j in range(len(arr[0])):
        new.append(arr[i][j] + arr[i-1][j])
    arr[i] = new

print(arr)

