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

import heapq
# from collections import deque
#
# INF = 1e9
# n,m = map(int,input().split())
# dic = {i+1:[] for i in range(n)}
#
# for i in range(m):
#     frm,to,much = map(int,input().split())
#     dic[frm].append((much,to))
#
# def getMinimumDistanceWhitQ(frm):
#     xx = deque()
#     distance = [INF] * (n + 1)
#     xx.append((0, frm))
#     distance[frm] = 0
#     count = []
#     while xx:
#         much,whr = xx.popleft()
#         count.append((much,whr))
#         if distance[whr] < much:
#             continue
#         for i in dic[whr]:
#             if much + i[0] <= distance[i[1]]:
#                 distance[i[1]] = much + i[0]
#                 xx.append((much + i[0],i[1]))
#     return distance,count
#
# def getMinimumDistance(frm):
#     xx = []
#     distance = [INF] * (n + 1)
#     heapq.heappush(xx, (0, frm))
#     distance[frm] = 0
#     count = []
#     while xx:
#         much,whr = heapq.heappop(xx)
#         count.append((much, whr))
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
# import sys
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
# arr = []
#
# for i in range(n): arr.append(list(map(int,input().split())))
#
# for i in arr:
#     for j in range(1,len(i)):
#         i[j] += i[j-1]
#
# for i in range(1,len(arr)):
#     new = []
#     for j in range(len(arr[0])):
#         new.append(arr[i][j] + arr[i-1][j])
#     arr[i] = new
#
# for i in range(m):
#     a,b,c,d = map(int,input().split())
#     big = arr[c-1][d-1]
#     rightSmall = 0
#     leftSmall = 0
#     totalSmall = 0
#     if a != 1:
#         rightSmall = arr[a-2][d-1]
#     if b != 1:
#         leftSmall = arr[c-1][b-2]
#     if rightSmall != 0 and leftSmall != 0:
#         totalSmall = arr[a-2][b-2]
#     print(big-rightSmall-leftSmall+totalSmall)

# 1753번 최단경로
# import sys
# import heapq
#
# input = sys.stdin.readline
# INF = 1e9
#
# n, m = map(int,input().split())
# dic = {i+1:[] for i in range(n)}
# distance = [INF for i in range(n+1)]
#
# start = int(input())
#
#
# for i in range(m):
#     frm,to,much = map(int,input().split())
#     dic[frm].append((much,to))
#
# q = []
# heapq.heappush(q,(0,start))
#
# while q:
#     much,now = heapq.heappop(q)
#
#     if distance[now] < much:
#         continue
#
#     distance[now] = much
#
#     for i in dic[now]:
#         if distance[i[1]] > much+i[0]:
#             heapq.heappush(q,(much+i[0],i[1]))
#             distance[i[1]] = much+i[0]
#
# for i in range(1,len(distance)):
#     if distance[i] == INF:
#         print('INF')
#     else:
#         print(distance[i])

# 11404번 플로이드
# import sys
# input = sys.stdin.readline
#
# INF = 1e9
# n = int(input())
# m = int(input())
# total = [[INF for _ in range(n)] for _ in range(n)]
#
# for i in range(n): total[i][i] = 0
#
# for i in range(m):
#     a,b,c = map(int,input().split())
#     if total[a-1][b-1] > c:
#         total[a-1][b-1] = c
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             total[i][j] = min(total[i][j], total[i][k] + total[k][j])
#
# for i in range(n):
#     for j in range(n):
#         if total[i][j] == INF:
#             total[i][j] = 0
#
# for i in total:
#     print(' '.join(map(str,i)))

#11053번 가장 긴 증가하는 부분 수열
# n = int(input())
# arr = list(map(int,input().split()))
# answer = [1]
#
# for i in range(1,n):
#     if arr[i] == arr[i-1]:
#         answer.append(answer[i-1])
#     else:
#         a = []
#         for k in range(i,-1,-1):
#             if arr[k] < arr[i]:
#                 a.append(answer[k])
#         if a != []:
#             answer.append(max(a)+1)
#         else:
#             answer.append(1)
#
# print(max(answer))

#10830번 행렬 제곱
# n,b = map(int,input().split())
# matrix = []
# for i in range(n): matrix.append(list(map(int,input().split())))
#
# def powMaxtrix(mat1,mat2,c):
#     if mat2 == []:
#         new = [[0 for i in range(len(mat1))] for i in range(len(mat1))]
#         for i in range(len(mat1)):
#             for j in range(len(mat1)):
#                 new[i][j] = mat1[i][j] % c
#         return new
#
#     new = [[0 for i in range(len(mat1))] for i in range(len(mat1))]
#     for i in range(len(mat1)):
#         a = [j%c for j in mat1[i]]
#         for j in range(len(mat1)):
#             b = []
#             for k in range(len(mat2)):
#                 b.append(mat2[k][j]%c)
#             new[i][j] = sum([v*x for v,x in zip(a,b)]) % c
#
#     return new
#
# def ultar(a,b,c):
#     if b == 1:
#         return powMaxtrix(a,[],c)
#     if b == 2:
#         return powMaxtrix(a,a,c)
#     if b % 2 == 0 :
#         result = ultar(a,b//2,c)
#         return powMaxtrix(result,result, c)
#     else:
#         result = ultar(a, b // 2, c)
#         return powMaxtrix(powMaxtrix(result,result, c),a,c)
#
# for i in ultar(matrix,b,1000):
#     print(' '.join(map(str,i)))

#11725번 트리의 부모찾기
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# dic = {i+1:[] for i in range(n)}
# visited = [False for i in range(n+1)]
# answer = [0 for _ in range(n+1)]
#
# for i in range(n-1):
#     a, b = map(int,input().split())
#     dic[a].append(b)
#     dic[b].append(a)
#
# q = deque()
# q.append(1)
#
# while q:
#     now = q.popleft()
#
#     if visited[now] == True:
#         continue
#     visited[now] = True
#
#     for i in dic[now]:
#         if visited[i] == False:
#             answer[i] = now
#             q.append(i)
#
# for i in answer[2:]:
#     print(i)

# 14502번 연구소
# from itertools import combinations
# from collections import deque
#
# l,m = map(int,input().split())
# total = []
# zero = []
# virus = []
# answer = 0
# dm = [1,0,-1,0]
# dl = [0,1,0,-1]
# for i in range(l):
#     total.append(list(map(int,input().split())))
#
# for i in range(l):
#     for j in range(m):
#         if total[i][j] == 0:
#             zero.append((i,j))
#         elif total[i][j] == 2:
#             virus.append((i,j))
#
# for candidate in list(combinations(zero,3)):
#     newTotal = [i[:] for i in total]
#     for one in candidate:
#         newTotal[one[0]][one[1]] = 1
#     q = deque(virus[:])
#     while q:
#         now = q.popleft()
#         for a,b in zip(dl,dm):
#             if l > now[0]+a >= 0 and m > now[1]+b >= 0:
#                 if newTotal[now[0]+a][now[1]+b] == 0:
#                     newTotal[now[0]+a][now[1]+b] = 2
#                     q.append((now[0]+a,now[1]+b))
#     count = 0
#     for i in range(l):
#         for j in range(m):
#             if newTotal[i][j] == 0:
#                 count += 1
#     if answer < count:
#         answer = count
#
# print(answer)

# 15686번 치킨 배달
# from itertools import combinations
#
# n,m = map(int,input().split())
# total = []
# home = []
# chicken = []
# answer = 1e9
#
# for i in range(n):
#     total.append(list(map(int,input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if total[i][j] == 1:
#             home.append((i,j))
#         elif total[i][j] == 2:
#             chicken.append((i,j))
#
# for candidate in list(combinations(chicken,m)):
#     count = 0
#     for h in home:
#         mini = []
#         for one in candidate:
#             mini.append(abs(h[0]-one[0])+abs(h[1]-one[1]))
#         count += min(mini)
#     if answer > count:
#         answer = count
#
# print(answer)

# 1916번 최소비용 구하기
# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n = int(input())
# dic = {i+1:[] for i in range(n)}
# m = int(input())
# distance = [1e9] * (n+1)
#
# for i in range(m):
#     frm,to,cost = map(int,input().split())
#     dic[frm].append((to,cost))
#
# start,end = map(int,input().split())
#
# q = []
# distance[start] = 0
# heapq.heappush(q,(0,start))
#
# while q:
#     cost, frm = heapq.heappop(q)
#     if distance[frm] < cost:
#         continue
#     if frm == end:
#         break
#     for i in dic[frm]:
#         if cost + i[1] < distance[i[0]]:
#             distance[i[0]] = cost+i[1]
#             heapq.heappush(q,(cost+i[1],i[0]))
#
# print(distance[end])

#2638번 치즈
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n,m = map(int,input().split())
# total = []
# cheese = []
# dm = [1,0,-1,0]
# dl = [0,1,0,-1]
#
# for i in range(n):
#     total.append(list(map(int,input().split())))
#
# for i in range(n):
#     for j in range(m):
#         if total[i][j] == 1:
#             cheese.append(((i,j)))
#
# answer = 0
#
# def blew():
#     global n
#     global m
#     q = deque()
#     q.append([0,0])
#     total[0][0] = 9
#     while q:
#         now = q.popleft()
#         for a, b in zip(dl, dm):
#             if n > now[0] + a >= 0 and m > now[1]+b >= 0 and total[now[0] + a][now[1] + b] == 0:
#                 total[now[0] + a][now[1] + b] = 9
#                 q.append([now[0] + a,now[1] + b])
#
# def reset():
#     for i in range(n):
#         for j in range(m):
#             if total[i][j] == 9:
#                 total[i][j] = 0
#
# while cheese:
#     blew()
#     bucket = []
#     for i in cheese:
#         count = 0
#         for a, b in zip(dl, dm):
#             if total[i[0] + a][i[1] + b] == 9:
#                 count += 1
#         if count >= 2:
#             bucket.append(i)
#     for k in bucket:
#         total[k[0]][k[1]] = 0
#         cheese.remove(k)
#     answer += 1
#     reset()
#
# print(answer)

#1865번 웜홀
# import sys
# import heapq
#
# input = sys.stdin.readline
# tc = int(input())
#
# for _ in range(tc):
#     n,m,w = map(int,input().split())
#     dic = {i+1:[] for i in range(n)}
#
#     for _ in range(m):
#         start,end,time = map(int,input().split())
#         dic[start].append((end,time))
#         dic[end].append((start,time))
#     for _ in range(w):
#         start,end,time = map(int,input().split())
#         dic[start].append((end,-time))
#
#     for k in range(1,n+1):
#         distance = [1e9] * (n+1)
#         q = []
#         heapq.heappush(q,(0,k))
#         distance[k] = 0
#         count = 0
#         while q:
#             cost,now = heapq.heappop(q)
#             if distance[now] < cost:
#                 continue
#             if now == k:
#                 count += 1
#                 if count == 2:
#                     break
#             for i in dic[now]:
#                 if cost+i[1] < distance[i[0]]:
#                     distance[i[0]] = cost+i[1]
#                     heapq.heappush(q,(cost+i[1],i[0]))
#
#         if distance[k] < 0 :
#             print('YES')
#             break
#     else:
#         print('NO')




