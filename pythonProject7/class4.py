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

# n = int(input())
#
# if (n%4 == 0 and n%100 != 0) or n%400 == 0:
#     print(1)
# else:
#     print(0)
# from collections import deque
#
# total = deque(input())
# answer = 0
# bucket = ['c=','c-','dz=','d-','lj','nj','s=','z=']
#
# while total:
#     now = total.popleft()
#     if now in ['c','d','l','n','s','z'] and len(total) >= 1:
#         if now + total[0] in bucket:
#             answer += 1
#             total.popleft()
#         elif len(total) >= 2 and now + total[0] + total[1] == 'dz=':
#             answer += 1
#             total.popleft()
#             total.popleft()
#         else:
#             answer += 1
#     else:
#         answer += 1
#
# print(answer)

# a = [1,2,3,3,3,4,4,5,5]
# i = 0
# answer = []
#
# while i < len(a)-1:
#     if i < len(a)-1 and a[i] != a[i+1]:
#         i+=1
#     else:
#         count = 1
#         while i < len(a)-1 and a[i] == a[i+1]:
#             count += 1
#             i += 1
#         answer.append(count)
# print(answer)

# def solution(n):
#     an = ''
#     while n != 0:
#         an += str(n%3)
#         n = n//3
#     answer = 0
#     for i,v in enumerate(str(int(an))[::-1]):
#         answer += int(v)*(3**i)
#     return answer
#
#
# print(solution(125))

# 트리순회
# n = int(input())
# dic = {}
#
# for i in range(n):
#     node,right,left = input().split()
#     dic[node] = [right,left]
#
# oneAnswer = ''
# def one(root):
#     global oneAnswer
#     oneAnswer += root
#     if dic[root][0] != '.':
#         one(dic[root][0])
#     if dic[root][1] != '.':
#         one(dic[root][1])
#
# secondAnswer = ''
# def two(root):
#     global secondAnswer
#     if dic[root][0] != '.':
#         two(dic[root][0])
#     secondAnswer += root
#     if dic[root][1] != '.':
#         two(dic[root][1])
#
# thirdAnswer = ''
# def third(root):
#     global thirdAnswer
#     if dic[root][0] != '.':
#         third(dic[root][0])
#     if dic[root][1] != '.':
#         third(dic[root][1])
#     thirdAnswer += root
#
# one('A')
# two('A')
# third('A')
#
# print(oneAnswer)
# print(secondAnswer)
# print(thirdAnswer)

# 이진 검색 트리
# import sys
# input = sys.stdin.readline
#
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class NodeMgmt:
#     def __init__(self,head):
#         self.head = head
#
#     def insert(self,value):
#         self.currunt_node = self.head
#         while True:
#             if value < self.currunt_node.value:
#                 if self.currunt_node.left != None:
#                     self.currunt_node = self.currunt_node.left
#                 else:
#                     self.currunt_node.left = Node(value)
#                     break
#             else:
#                 if self.currunt_node.left != None:
#                     self.
#
# total = []
#
# while True:
#     try:
#         total.append(int(input()))
#     except:
#         break
# l,m,k = map(int, input().split(' '))
# total = [list(map(int,input().split(' '))) for _ in range(l)]
# where = []
#
# for i in range(l):
#     if total[i][0] == -1:
#         where.append(i)
#
# def upper():
#     a = [0]
#     a.extend(total[where[0]][1:])
#     a.extend([i[-1] for i in total[:where[0]]][::-1])
#     a.extend(total[0][:-1][::-1])
#     a.extend([i[0] for i in total[1:where[0]-1]])
#
#     index = 0
#     for i in range(1,m):
#         total[where[0]][i] = a[index]
#         index += 1
#     for i in range(where[0]-1,-1,-1):
#         total[i][-1] = a[index]
#         index += 1
#     for i in range(m-2,-1,-1):
#         total[0][i] = a[index]
#         index += 1
#     for i in range(1,where[0]):
#         total[i][0] = a[index]
#         index += 1
#
# def lower():
#     a = [0]
#     a.extend(total[where[1]][1:])
#     a.extend([i[-1] for i in total[where[1]+1:]])
#     a.extend(total[-1][:-1][::-1])
#     a.extend([i[0] for i in total[where[1]+2:-1]][::-1])
#
#     index = 0
#     for i in range(1,m):
#         total[where[1]][i] = a[index]
#         index += 1
#     for i in range(where[1]+1,l):
#         total[i][-1] = a[index]
#         index += 1
#     for i in range(m-2,-1,-1):
#         total[-1][i] = a[index]
#         index += 1
#     for i in range(l-2,where[1],-1):
#         total[i][0] = a[index]
#         index += 1
#
# def spread():
#     dm = [1,0,-1,0]
#     dl = [0,1,0,-1]
#     target = []
#     for i in range(l):
#         for j in range(m):
#             if total[i][j] != -1 and total[i][j] != 0:
#                 target.append([i,j])
#
#     dic = {str(x)+str(s): [] for s in range(m) for x in range(l)}
#
#     for i,j in target:
#         count = 0
#         for s in range(4):
#             if l > i+dl[s] >= 0 and m > j+dm[s] >= 0 and total[i+dl[s]][j+dm[s]] != -1:
#                 if str(i+dl[s])+str(j+dm[s]) in dic.keys():
#                     dic[str(i+dl[s])+str(j+dm[s])].append(total[i][j]//5)
#                 count += 1
#         total[i][j] -= (total[i][j]//5) * count
#
#     for i in dic.keys():
#         a,b = map(int,i)
#         for j in dic[i]:
#             total[a][b] += j


# def dust_move():
#     temp = [[0] * m for _ in range(l)]
#     for i in range(l):
#         for j in range(m):
#             if total[i][j] >= 5:
#                 val = 0
#                 if i - 1 >= 0 and total[i - 1][j] != -1:
#                     temp[i - 1][j] += total[i][j] // 5
#                     val += total[i][j] // 5
#                 # 하
#                 if i + 1 < l and total[i + 1][j] != -1:
#                     temp[i + 1][j] += total[i][j] // 5
#                     val += total[i][j] // 5
#                 # 좌
#                 if j - 1 >= 0 and total[i][j - 1] != -1:
#                     temp[i][j - 1] += total[i][j] // 5
#                     val += total[i][j] // 5
#                 # 우
#                 if j + 1 < m and total[i][j + 1] != -1:
#                     temp[i][j + 1] += total[i][j] // 5
#                     val += total[i][j] // 5
#                 temp[i][j] -= val
#     for i in range(l):
#         for j in range(m):
#             total[i][j] += temp[i][j]
#
# for i in range(k):
#     dust_move()
#     upper()
#     lower()
#
# answer = 0
#
# for i in range(l):
#     for j in range(m):
#         if total[i][j] > 0:
#             answer += total[i][j]
#
# print(answer)

#17413번 단어뒤집기
# word = list(input())
# answer = ''
# i = 0
# while i <= len(word)-1:
#     if word[i] == '<':
#         while word[i] != '>':
#             answer += word[i]
#             i += 1
#         answer += word[i]
#         i += 1
#     elif word[i] != ' ':
#         miniAnswer = ''
#         while i <= len(word)-1 and (word[i] != ' ' and word[i] != '<'):
#             miniAnswer += word[i]
#             i += 1
#         if i <= len(word)-1 and word[i] == ' ':
#             answer += miniAnswer[::-1] + ' '
#             i += 1
#         elif i >= len(word):
#             answer += miniAnswer[::-1]
#         elif word[i] == '<':
#             answer += miniAnswer[::-1]
# print(answer)

# n = int(input())
# m = int(input())
# total = list(input())
# answer = 0
# target = 'I' + 'OI'*n
# now = 0
# i = 0
#
# while i < len(total):
#     if total[i] == target[now]:
#         if now == len(target)-1:
#             answer += 1
#             now -= 1
#         else:
#             now += 1
#     else:
#         if total[i] == "I":
#             now = 1
#         else:
#             now = 0
#     i += 1
#
# print(answer)

# target = input()
# length = len(target)
# candidate = []
#
# def solution():
#     for i in range(length,length*2+1):
#         if i % 2 == 0:
#             k = 0
#             while True:
#                 if i//2-1-k < 0 or i//2-1+k+1 >= length:
#                     return i
#                 if target[i//2-1-k] == target[i//2-1+k+1]:
#                     k += 1
#                 else:
#                     break
#         else:
#             k = 1
#             while True:
#                 if i//2 - k < 0 or i // 2 + k >=length:
#                     return i
#                 if target[i//2-k] == target[i//2+k]:
#                     k += 1
#                 else:
#                     break
#
# print(solution())



# n = int(input())
# answer = 0
# for i in range(n):
#     word = input()
#     dic = {}
#     index = 0
#     isRight = True
#
#     while index < len(word):
#         if word[index] not in dic.keys():
#             dic[word[index]] = 1
#             while index < len(word)-1 and word[index] == word[index+1]:
#                 dic[word[index]] += 1
#                 index += 1
#             index += 1
#         else:
#             isRight = False
#             break
#
#     if isRight:
#         answer += 1
#
# print(answer)

# arr = []
# for i in range(4): arr.append(list(map(int,list(input()))))
#
# n = int(input())
# orders = []
# turned = [False]*4
#
# for i in range(n): orders.append(list(map(int,input().split())))
#
# def turn(target,direction):
#     dx = [-1,1]
#     turned[target] = True
#     for i in dx:
#         if 3 >= target + i >= 0:
#             if target+i < target:
#                 if arr[target+i][2] != arr[target][6] and not turned[target+i]:
#                     turn(target+i,-direction)
#             else:
#                 if arr[target+i][6] != arr[target][2] and not turned[target+i]:
#                     turn(target+i,-direction)
#
#     if direction == 1:
#         new = arr[target].pop(-1)
#         arr[target].insert(0,new)
#     else:
#         new = arr[target].pop(0)
#         arr[target].append(new)
#
# for order in orders:
#     turned = [False] * 4
#     turn(order[0]-1,order[1])
#
# answer = 0
#
# for i,v in enumerate(arr):
#     if v[0] == 1:
#         answer += 2**i
#
# print(answer)

# 드래곤 커브
# n = int(input())
# arr = []
# total = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#
# def grow(dragon):
#     for i in range(len(dragon)-1,0,-1):
#         if dragon[i][0] - dragon[i-1][0] == 1:
#             dragon.append([dragon[-1][0],dragon[-1][1]-1])
#         elif dragon[i][0] - dragon[i-1][0] == -1:
#             dragon.append([dragon[-1][0],dragon[-1][1]+1])
#         elif dragon[i][1] - dragon[i-1][1] == 1:
#             dragon.append([dragon[-1][0]+1, dragon[-1][1]])
#         elif dragon[i][1] - dragon[i-1][1] == -1:
#             dragon.append([dragon[-1][0]-1, dragon[-1][1]])
#     return dragon
#
# for one in arr:
#     mini = [[one[0],one[1]]]
#     if one[2] == 0:
#         mini.append([one[0]+1,one[1]])
#     elif one[2] == 1:
#         mini.append([one[0],one[1]-1])
#     elif one[2] == 2:
#         mini.append([one[0]-1,one[1]])
#     elif one[2] == 3:
#         mini.append([one[0],one[1]+1])
#     for i in range(one[3]):
#         mini = grow(mini)
#     for i in mini:
#         total.append(i)
#
# total = list(set([tuple(i) for i in total]))
#
# answer = 0
#
# for i in range(0,100):
#     for j in range(0,100):
#         for k in [(i,j),(i,j+1),(i+1,j),(i+1,j+1)]:
#             if k not in total:
#                 break
#         else:
#             answer += 1
#
# print(answer)

# 2607번 비슷한 단어
# n = int(input())
# mom = input()
# compare = []
# answer = 0
#
# for i in range(n-1):
#     compare.append(input())
#
# def comparing(word1,word2):
#     if set(word1) != set(word2):
#         return False
#     for i in set(word1):
#         if word1.count(i) != word2.count(i):
#             return False
#     return True
#
# for one in compare:
#     for i in range(65,91):
#         new1 = list(mom)
#         if chr(i) in new1:
#             new1.remove(chr(i))
#         if comparing(new1,one):
#             answer += 1
#             break
#
#         new2 = list(mom)
#         new2.append(chr(i))
#         if comparing(new2,one):
#             answer += 1
#             break
#         continued = True
#         for j in range(len(mom)):
#             new3 = list(mom)
#             new3[j] = chr(i)
#             if comparing(new3,one):
#                 answer += 1
#                 continued = False
#                 break
#         if not continued:
#             break
# print(answer)

# 15683번 감시
# from itertools import product
# from collections import deque
# import copy
# l,m = map(int,input().split())
# total = [list(map(int,input().split())) for _ in range(l)]
# cctv = []
# answers = []
#
# for i in range(l):
#     for j in range(m):
#         if total[i][j] == 1:
#             cctv.append([(i, j),deque([0,1,0,0])])
#         elif total[i][j] == 2:
#             cctv.append([(i, j), deque([0, 1, 0, 1])])
#         elif total[i][j] == 3:
#             cctv.append([(i, j), deque([1, 1, 0, 0])])
#         elif total[i][j] == 4:
#             cctv.append([(i, j), deque([1, 1, 1, 0])])
#         elif total[i][j] == 5:
#             cctv.append([(i, j), deque([1, 1, 1, 1])])
#
# for i in product('ABCD',repeat=len(cctv)):
#     copyedTotal = copy.deepcopy(total)
#     copyedCCTV = copy.deepcopy(cctv)
#     for index,one in enumerate(copyedCCTV):
#         if i[index] == 'B':
#             for _ in range(1):
#                 copyedCCTV[index][1].appendleft(copyedCCTV[index][1].pop())
#         elif i[index] == 'C':
#             for _ in range(2):
#                 copyedCCTV[index][1].appendleft(copyedCCTV[index][1].pop())
#         elif i[index] == 'D':
#             for _ in range(3):
#                 copyedCCTV[index][1].appendleft(copyedCCTV[index][1].pop())
#
#     for one in copyedCCTV:
#         for x in range(4):
#             if one[1][x] == 1:
#                 if x == 0:
#                     c = 1
#                     while True:
#                         if l > one[0][0]-c >= 0 and copyedTotal[one[0][0]-c][one[0][1]] != 6:
#                             if copyedTotal[one[0][0]-c][one[0][1]] == 0:
#                                 copyedTotal[one[0][0]-c][one[0][1]] = '#'
#                             c += 1
#                         else:
#                             break
#                 elif x == 1:
#                     c = 1
#                     while True:
#                         if m > one[0][1] + c >= 0 and copyedTotal[one[0][0]][one[0][1]+c] != 6:
#                             if copyedTotal[one[0][0]][one[0][1]+c] == 0:
#                                 copyedTotal[one[0][0]][one[0][1]+c] = '#'
#                             c += 1
#                         else:
#                             break
#                 elif x == 2:
#                     c = 1
#                     while True:
#                         if l > one[0][0] + c >= 0 and copyedTotal[one[0][0]+c][one[0][1]] != 6:
#                             if copyedTotal[one[0][0]+c][one[0][1]] == 0:
#                                 copyedTotal[one[0][0]+c][one[0][1]] = '#'
#                             c += 1
#                         else:
#                             break
#                 elif x == 3:
#                     c = 1
#                     while True:
#                         if m > one[0][1] - c >= 0 and copyedTotal[one[0][0]][one[0][1]-c] != 6:
#                             if copyedTotal[one[0][0]][one[0][1]-c] == 0:
#                                 copyedTotal[one[0][0]][one[0][1]-c] = '#'
#                             c += 1
#                         else:
#                             break
#     miniAnswer = 0
#     for a in copyedTotal:
#         for j in a:
#             if j == 0:
#                 miniAnswer += 1
#     answers.append(miniAnswer)
#
# print(min(answers))

#1987번 알파벳
# import copy
#
# l,m = map(int,input().split())
# arr = [list(input()) for _ in range(l)]
# total = []
#
# def dfs(startPoint,until):
#     dm = [0,0,1,-1]
#     dl = [1,-1,0,0]
#     count = 0
#     for a,b in zip(dl,dm):
#         if l > startPoint[0]+a >= 0 and m > startPoint[1]+b >= 0:
#             if arr[startPoint[0]+a][startPoint[1]+b] not in until:
#                 vv = copy.deepcopy(until)
#                 vv.append(arr[startPoint[0]+a][startPoint[1]+b])
#                 dfs([startPoint[0]+a,startPoint[1]+b],vv)
#                 count += 1
#
#     if count == 0:
#         total.append(len(until))
#
# dfs([0,0],[arr[0][0]])
#
# print(max(total))
# def solution(stones, k):
#     mini = min(stones)
#     maxi = max(stones)
#
#     def isPossible(number):
#         i = 0
#         while i < len(stones):
#             if stones[i] <= number:
#                 count = 0
#                 while i < len(stones) and stones[i] <= number:
#                     i += 1
#                     count += 1
#                 if count >= k:
#                     return False
#             else:
#                 i += 1
#         return True
#
#     answer = 0
#
#     while mini <= maxi:
#         pivot = (mini + maxi) // 2
#         print(pivot, mini, maxi)
#         print(isPossible(pivot))
#         if isPossible(pivot):
#             answer = pivot
#             mini = pivot + 1
#         else:
#             maxi = pivot - 1
#
#     return answer

# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1] - x[0])
#     checked = [False] * len(routes)
#
#     def cal(one):
#         count = 0
#         arr = []
#         count2 = 0
#         arr2 = []
#
#         for i, v in enumerate(routes):
#             if v[0] <= one[0] <= v[1] and not checked[i]:
#                 count += 1
#                 arr.append([i, v])
#             if v[0] <= one[1] <= v[1] and not checked[i]:
#                 count2 += 1
#                 arr2.append([i, v])
#
#         if count >= count2:
#             return arr
#         else:
#             return arr2
#
#     answer = 0
#
#     for i in routes:
#
#         if False not in checked:
#             break
#         if checked[routes.index(i)] == False:
#             deletedCar = cal(i)
#             answer += 1
#             for k in deletedCar:
#                 checked[k[0]] = True
#
#     return answer
#
# print(solution([ [-191, -107],[-184,-151],[-150,-102],[-171,-124],[-120,-114]]))

# 1213 팰린드롬 만들기

# n = input()
#
# if len(n) % 2 == 0:
#     answer = ''
#     n = sorted(n,reverse=True)
#     dic = {i:0 for i in set(n)}
#     for i in n:
#         dic[i] += 1
#     for i in dic.keys():
#         if dic[i] % 2 == 1:
#             print("I'm Sorry Hansoo")
#             break
#     else:
#         for i in range(len(n)):
#             if i % 2 == 1:
#                 answer += n[i]
#             else:
#                 answer = n[i]+answer
#     print(answer)
# else:
#     answer = ''
#     n = sorted(n, reverse=True)
#     dic = {i: 0 for i in set(n)}
#     for i in n:
#         dic[i] += 1
#     count = 0
#     whr = ''
#     for i in dic.keys():
#         if dic[i] % 2 == 1:
#             count += 1
#             whr = i
#     if count != 1:
#         print("I'm Sorry Hansoo")
#     else:
#         n.remove(whr)
#         for i in range(len(n)):
#             if i % 2 == 1:
#                 answer += n[i]
#             else:
#                 answer = n[i] + answer
#         answer = list(answer)
#         answer.insert(len(n)//2,whr)
#         answer = ''.join(answer)
#         print(answer)

# 1213 시리얼 번호
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(input())
# number = ['0','1','2','3','4','5','6','7','8','9']
# arr = sorted(arr,key= lambda x:(len(x),sum([int(i) for i in x if i in number]),x))
#
# for i in arr:
#     print(i)

# 12904번 A와 B
# start = input()
# end = input()
# can = False
#
# while len(end) >= len(start):
#     if end == start:
#         can = True
#         break
#     if end[-1] == 'B':
#         end = end[:-1][::-1]
#     else:
#         end = end[:-1]
#
# if can:
#     print(1)
# else:
#     print(0)


def solution(user_id, banned_id):
    ultar = []
    for i in banned_id:
        whr = []
        for index, v in enumerate(i):
            if v == '*':
                whr.append(index)
        copyed = user_id[:]
        for k in range(len(copyed)):
            aa = list(copyed[k])
            for kk in whr:
                if kk <= len(aa) - 1:
                    aa[kk] = '*'
            copyed[k] = ''.join(aa)

        mini = []
        for k, v in enumerate(copyed):
            if v == i:
                mini.append(user_id[k])
        ultar.append(mini)
    answer = set()

    def dfs(index, currentset):
        if len(currentset) == len(ultar):
            print(currentset)
            # answer.add(set(currentset))
            return

        for i in ultar[index]:
            if i not in currentset:
                new = currentset
                new.append(i)
                dfs(index + 1, new)

    dfs(0, [])
    print(answer)
    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])
