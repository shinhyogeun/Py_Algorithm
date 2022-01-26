# 1.큰 수의 법칙(30분)(53분까지)

#내 코드

'''length, howMany, cutline = list(map(int,input().split()))
arr = list(map(int,input().split())) ; arr.sort()
cycle = howMany//(cutline+1)
recycle = howMany%(cutline+1)
print(arr[-1]*(cycle*cutline+recycle)+arr[-2]*(cycle))'''

#갓동빈 코드
'''length, howMany, cutline = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
result = 0

while True:
    for i in range(cutline):
        if howMany == 0:
            break
        result += arr[-1]
        howMany -= 1
    if howMany == 0:
        break
    result += arr[-2]
    howMany -= 1
print(result)'''



# 2.숫자 카드 게임(30분)(1시 38분까지)

'''row,col = map(int,input().split())
resultCompare = []
squre = [[0]*col for i in range(row)]
for i in range(row):
    squre[i] = list(map(int,input().split()))

for i in range(row):
    squre[i].sort()
    resultCompare.append(squre[i][0])

print(sorted(resultCompare)[-1])'''

# 3. 1이 될 때까지(30분)(2시 1분까지)
'''mother, sun = map(int,input().split())
result = 0

while True:
    if mother%sun != 0:
        mother -= 1
    elif mother%sun == 0:
        mother = mother/sun
    result += 1
    if mother == 1:
        print(result)
        break

print(1//2)'''

# 4. 상하좌우

'''squreSize = int(input())
startPoint = [1,1]
root = list(input())
for i in root:
    if i == "R":
        if startPoint[1] < squreSize:
            startPoint = [startPoint[0],startPoint[1]+1]
    elif i == "u":
        if startPoint[0] < 1:
            startPoint = [startPoint[0]-1, startPoint[1]]
    elif i == "D":
        if startPoint[0] < squreSize:
            startPoint = [startPoint[0]+1, startPoint[1]]
    elif i == "L":
        if startPoint[1] < 1:
             startPoint = [startPoint[0], startPoint[1]-1]

print(startPoint[0], startPoint[1])'''

# 4. 시각

# 내 풀이
'''a = int(input())
root = a//3
print((root*3600)+((a+1-root)*15*105))'''

#갓동빈 풀이
'''a = int(input())
count = 0

for i in range(a+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                count += 1
print(count)'''

# 4.2 왕실의 나이트

'''a = list(input())
row = int(a[1])
col = a[0]
mother = ["a","b","c","d","e","f","g"]
numcol = mother.index(col)+1
answer = [[0]*2 for j in range(8)]
count = 0
answer[0] = [row-2,numcol-1]
answer[1] = [row-2,numcol+1]
answer[2] = [row-1,numcol-2]
answer[3] = [row+1,numcol-2]
answer[4] = [row-1,numcol+2]
answer[5] = [row+1,numcol+2]
answer[6] = [row+2,numcol-1]
answer[7] = [row+2,numcol+1]

for i in answer:
    if 1<=i[0]<=8 and 1<=i[1]<=8:
        count += 1
print(count)'''


# 4.3 게임 개발(개 어렵네..)

'''l,m = list(map(int,input().split()))
squre = [[0]*m for _ in range(l)]
nowX, nowY, nowDirection= list(map(int,input().split()))
count = 1
check = 0
for i in range(l):
    squre[i] = list(map(int,input().split()))
squre[nowX][nowY] = 9

# 그 위치에서 그 방향으로 이동가능하면 이동하고 아니면 회전해서 다시 판단하자!
def roll(startpotion,nowdirection):
    growth = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    global squre
    global check
    global count
    # 새로운 개척이 안될 때
    if squre[startpotion[0]+growth[nowdirection][0]][startpotion[1]+growth[nowdirection][1]] != 0:
        check += 1
        if check == 4:
            final(startpotion,nowdirection)
        else:
            nowdirection = nowdirection - 1 if nowdirection != 0 else 3
            roll(startpotion, nowdirection)
    # 새로운 개척이 될때
    else:
        check = 0
        count += 1
        squre[startpotion[0] + growth[nowdirection][0]][startpotion[1] + growth[nowdirection][1]] = 9
        startpotion = [startpotion[0]+growth[nowdirection][0],startpotion[1]+growth[nowdirection][1]]
        nowdirection = nowdirection - 1 if nowdirection != 0 else 3
        roll(startpotion, nowdirection)

def final(startpotion,nowdirection) :
    global check
    global count
    back = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    # 백을치기 가능할 때
    if squre[startpotion[0] + back[nowdirection][0]][startpotion[1] + back[nowdirection][1]] != 1:
        check = 0
        startpotion = [startpotion[0] + back[nowdirection][0], startpotion[1] + back[nowdirection][1]]
        roll(startpotion, nowdirection)
    # 백을치기 안될 때
    else:
        print(count)
roll([nowX,nowY],nowDirection)'''

# 민상이의 문제

'''def factorial(num):
    result = 0
    if num <= 0:
        return 0
    for i in range(num):
        result = result + (i+1)
    return result

a = int(input())
answer_arr = [0] * a
for i in range(a):
    c,d = list(map(int,input().split()))
    answer_arr[i] = d-c
t = 0
beforemove = 1
count = 1
aim = answer_arr[t]-1 # 처음에 한칸 이동한 후에 시작하는 거다.
while t < a:
    arr = []
    if aim == 0:
        print(1)
        t += 1
    else:
        candidate = [beforemove-1, beforemove, beforemove+1]
        for i in candidate:
            if (i != 0 and aim-i >= factorial(i-1)):
                arr.append(i)
        if aim - sorted(arr)[-1] != 0:
            count += 1
            beforemove = sorted(arr)[-1]
            aim = aim-sorted(arr)[-1]
        else:
            count += 1
            print(count)
            if t < a-1 : aim = answer_arr[t+1] - 1
            t += 1
            count = 1'''

# 간단한 재귀함수 표현
'''def recursive_function(i):
    if i == 100:
        return
    print(i,"번째 재귀함수에서 ", i+1,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀함수 종료")
recursive_function(1)'''

#깊이 우선탐색
#내가 하는 코드 (도중에 빡쳐서 그만 둠)
'''def dfs(startpoint):
    if check[startpoint-1] == False:
        check[startpoint-1] = True
        print(startpoint, sep=" ")
    candidate = []
    for i in graph[startpoint-1]:
        if check[i-1] == False:
            dfs(min(candidate))
    if len(candidate) > 0 :
    else:

        return
dfs(1)'''
#이쁜 코
'''graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4],
        [3, 5],
        [3, 4],
        [7],
        [6, 8],
        [1, 7],
    ]
vi = [False] * 9
def dfs2(graph,v,visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs2(graph,i,visited)

dfs2(graph,1,vi)

import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))'''


# def solution(numbers):
#     total = {i: False for i in range(10)}
#     answer = 0
#     for i in numbers:
#         if not total[i]:
#             total[i] = True
#
#     for i in total:
#         if total[i] != True: answer += i
#     return answer

# from itertools import product
#
# def solution(word):
#     total = ['A', 'E', 'I', 'O', 'U']
#     ultra = []
#     for i in range(1,6):
#         ultra += list(product(total, repeat=i))
#     ultra = sorted(ultra)
#     return ultra.index(tuple(word))+1
#
# print(solution('AAAE'))

# from collections import deque
#®
# def solution(enter, leave):
#     answer = [0 for i in range(len(enter))]
#     enter = deque(enter)
#     leave = deque(leave)
#     total = []
#     total.append(enter.popleft())
#     while leave:
#         if leave[0] not in total:
#             for i in total:
#                 answer[i-1] += 1
#             total.append(enter.popleft())
#             answer[total[-1]-1] = len(total)-1
#         else:
#             total.remove(leave.popleft())
#     return answer
#
# print(solution([1,4,2,3],[2,1,3,4]))
# print(solution([1,4,2,3],[2,1,4,3]))

# def dfs(total,i,j):
#     total[i][j] = 5
#     w = len(total[0])
#     h = len(total)
#     direction = [-1,0,1]
#     for a in direction:
#         for b in direction:
#             if (0<=i+a<h and 0<=j+b<w) and total[i+a][j+b] == 1:
#                 dfs(total,i+a,j+b)
#
#
# while True:
#      w,h = list(map(int,input().split()))
#      if w == 0 and h == 0: break
#      total = []
#      for i in range(h):
#          total.append(list(map(int,input().split())))
#      answer = 0
#      for i in range(h):
#          for j in range(w):
#              if total[i][j] == 1:
#                  answer += 1
#                  dfs(total,i,j)
#      print(answer)

# from collections import deque
#
# total = deque(list(input()))
# target = input()
# answer = 0
# now = ''
#
# while total:
#     now += total.popleft()
#     if now == target:
#         answer += 1
#         now = ''
#     elif not target.startswith(now) and len(now) > 1:
#         now = now[1:]
#     elif not target.startswith(now) and len(now) == 1:
#         now = ''
#
# print(answer)

# from collections import deque
# n = int(input())
# total = deque(map(int,input().split()))
#
# a1 = [total.popleft(), total.popleft()]
#
# while total:
#     newOne = total.popleft()
#     a2 = max(0,a1[0],newOne)
#     if a2 == 0:
#
#
# print(a2)


# total = ''.join(input().split(' '))
# if total == '12345678':
#     print('ascending')
# elif total == '87654321':
#     print('descending')
# else:
#     print('mixed')

# from itertools import combinations
#
# number, total = map(int,input().split())
# target = map(int,input().split())
# real = sorted(list([sum(i) for i in combinations(target,3)]))
# a = [i for i in real if i - total <= 0]
# if len(a) == 0:
#     print(real[-1])
# else:
#     print(a[-1])

# n = int(input())
# target = [int(input()) for i in range(n)]
# stack = []
# answer = []
#
# for i in range(1,n+1):
#     stack.append(i)
#     answer.append('+')
#     if (stack[-1] == target[0]):
#         while len(stack)!=0 and stack[-1] == target[0]:
#             stack.pop()
#             answer.append('-')
#             target.pop(0)
#
# if(len(stack)!=0):
#     print('NO')
# else:
#     for i in answer: print(i)

# n = int(input())
#
# for i in range(n):
#     length, target = map(int,input().split())
#     all = [[i,v] for v,i in enumerate(list(map(int,input().split())))]
#     count = 1
#     while all != []:
#         if all[0][0] >= max([i[0] for i in all]):
#             if(all[0][1] == target):
#                 print(count)
#                 break
#             else:
#                 all.pop(0)
#                 count += 1
#         else:
#             all.append(all.pop(0))



# import sys
#
# n = int(input())
#
# for i in range(n):
#     inputs = list(sys.stdin.readline().rstrip())
#     answerLeft = []
#     answerRight = []
#     cursor = 0
#     for i in inputs:
#         if i == '<':
#             if answerLeft != []:
#                 answerRight.append(answerLeft.pop())
#         elif i == '>':
#             if answerRight != []:
#                 answerLeft.append(answerRight.pop())
#         elif i == '-':
#             if answerLeft != []:
#                 answerLeft.pop()
#         else:
#             answerLeft.append(i)
#             cursor += 1
#     print(''.join(answerLeft)+''.join(answerRight[::-1]))

# import hashlib
#
# inp = input()
# print(hashlib.sha256(inp.encode()).hexdigest())


# n = int(input())
# total = list(map(int,input().split()))
# m = int(input())
# target = list(map(int,input().split()))
# total = sorted(total)
# answer = []
# for i in range(m):
#     start = 0
#     end = len(total)-1
#     while start <= end:
#         pivot = (start + end) // 2
#         if total[pivot] == target[i]:
#             answer.append(1)
#             break
#         elif total[pivot] > target[i]:
#             end = pivot-1
#         elif total[pivot] < target[i]:
#             start = pivot+1
#     if start > end:
#         answer.append(0)
# for i in answer:
#     print(i)

# n = int(input())
#
# for i in range(n):
#     m = int(input())
#     total = {}
#     for i in range(m):
#         frm,to = input().split()
#         total[frm] = to

# n = int(input())
# a = [[] for i in range(200)]
# for i in range(n):
#     age,name = input().split()
#     age = int(age)
#     a[age-1].append(name)
#
# for i,v in enumerate(a):
#     for j in v:
#         print(i+1 , j)


# n = int(input())
# pibo = [0,1]
#
# def pibo(a):
#     if a == 1 :
#         return 1
#     if a == 0 :
#         return 0
#     else:
#         return pibo(a - 2) + pibo(a - 1)
#
# print(pibo(n))

# N,r,c = map(int,input().split())
#
# answer = 0
#
# def find(N,r,c):
#     global answer
#     if N == 0: return
#     if 0 <= r <= 2 ** (N - 1)-1 and 0 <= c <= 2 ** (N-1)-1:
#         return find(N - 1, r, c)
#     elif 0 <= r <= 2 ** (N - 1)-1 and 2 ** (N - 1) <= c <= 2 ** (N)-1:
#         answer += 2**(2*N)/4
#         return find(N - 1, r, c - 2 ** (N - 1))
#     elif 2 ** (N - 1) <= r <= 2 ** (N)-1 and 0 <= c <= 2 ** (N - 1)-1:
#         answer += (2**(2*N)/4) * 2
#         return find(N - 1, r - 2 ** (N - 1), c)
#     elif 2 ** (N - 1) <= r <= 2 ** (N) - 1 and 2 ** (N - 1) <= c <= 2 ** (N)-1:
#         answer += (2**(2*N)/4) * 3
#         return find(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1))
#
# find(N,r,c)
# print(int(answer))


# n = int(input())
# for i in range(n):
#     arr = [i for i in range(1,int(input())+1)]
#     answer = []
#     def check(index,value):
#         global arr
#         if index == len(arr)-1 and value!= '' and (eval(value.replace(" ",""))) == 0: return answer.append(value)
#         if index == len(arr)-1: return
#         check(index+1,value+'+'+str(arr[index+1]))
#         check(index+1,value+'-'+str(arr[index+1]))
#         check(index+1,value+' '+str(arr[index+1]))
#     check(0, '1')
#     for i in sorted(answer):print(i)
#     print()

# import sys
#
# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# for i in sorted(arr):
#     print(i)


# n,k = map(int, input().split())
# arr = list(map(int,input().split()))
# print(sorted(arr)[k-1])

# total = input()
# target = input()
# answer = 0
# while total:
#     if total.startswith(target):
#         answer += 1
#         for i in range(len(target)):
#             total = total[1:]
#     else:
#         total = total[1:]
# print(answer)

# n = int(input())
# dic = {}
# for i in range(n):
#     name = input()
#     if name in dic:
#         dic[name] += 1
#     else:
#         dic[name] = 0
#
# print(sorted(dic.items(),key=lambda x:(-x[1],x[0]))[0][0])

# l, m= map(int,input().split())
# col = [False for i in range(l)]
# row = [False for i in range(m)]
# for i in range(l):
#     a = list(input())
#     for j,k in enumerate(a):
#         if k == 'X':
#             col[i] = True
#             row[j] = True
# print(max(col.count(False),row.count(False)))

# n = int(input())

# tree = {}
# for i in range(n):
#     node,frm,to = input().split()
#     tree[node] = [frm,to]
#
# answer = []

# def firstCicle(node):
#     answer.append(node)
#     if tree[node][0] != '.': firstCicle(tree[node][0])
#     if tree[node][1] != '.': firstCicle(tree[node][1])

# def middleCicle(node):
#     if tree[node][0] != '.': middleCicle(tree[node][0])
#     answer.append(node)
#     if tree[node][1] != '.': middleCicle(tree[node][1])

# def endCicle(node):
#     if tree[node][0] != '.': endCicle(tree[node][0])
#     if tree[node][1] != '.': endCicle(tree[node][1])
#     answer.append(node)

# firstCicle('A')
# print(''.join(answer))
# answer = []
# middleCicle('A')
# print(''.join(answer))
# answer = []
# endCicle('A')
# print(''.join(answer))
# answer = []

# import heapq
# import sys
#
# heap = []
# n = int(sys.stdin.readline())

# for i in range(n):
#     inp = int(sys.stdin.readline())
#     if inp == 0:
#         if len(heap) != 0:
#             print(heapq.heappop(heap))
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, inp)

# import heapq
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# total = []
# for i in range(n):
#     heapq.heappush(total,int(input()))
#
# if len(total) == 1: print(0)
# elif len(total) == 2: print(sum(total))
# else:
#     answer = 0
#     while len(total)!= 1:
#         now = heapq.heappop(total) + heapq.heappop(total)
#         answer += now
#         heapq.heappush(total,now)
#     print(answer)

# from collections import deque
#
# n, m = map(int,input().split())
# dic = {i:[] for i in range(1,n+1)}
# weight = []
#
# for i in range(m):
#     frm,to,cost = map(int,input().split())
#     weight.append(cost)
#     dic[frm].append([to,cost])
#     dic[to].append([frm, cost])
#
# weight = sorted(list(set(weight)))
# start,end = map(int,input().split())
#
# a = weight[0]
# b = weight[-1]
# answer = 0
#
# while a <= b:
#     pivot = (a + b) // 2
#     newDic = {}
#     for i in dic:
#         newDic[i] = []
#         for j in dic[i]:
#             if j[1] >= pivot:
#                 newDic[i].append(j)
#     queue = deque()
#     queue.append(start)
#     visited = []
#     isPossible = False
#     while queue:
#         now = queue.popleft()
#         if now not in visited:
#             visited.append(now)
#             for i in newDic[now]:
#                 queue.append(i[0])
#         if end in visited:
#             answer = pivot
#             isPossible = True
#             break
#     if isPossible: a = pivot+1
#     else: b = pivot-1
#
# print(answer)

# from bisect import bisect_left, bisect_right
# nums = [0,10,20,30,40,50,60,70,80,90]
# n = 90
# print(bisect_left(nums, n))
# print(bisect_right(nums, n))

# import sys
# from bisect import bisect_left
#
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
# house = []
# for i in range(n): house.append(int(input()))
# house = sorted(house)
#
# start = 1
# end = house[-1]
# answer = 0
#
# while start <= end:
#     pivot = (start+end)//2
#     count = 1
#     now = house[0]
#     isPossible = False
#
#     while bisect_left(house,now + pivot) != len(house):
#         count += 1
#         if count == m :
#             isPossible = True
#             break
#         now = house[bisect_left(house,now + pivot)]
#
#     if isPossible:
#         answer = pivot
#         start = pivot+1
#     else:
#         end = pivot-1
#
# print(answer)


# n = int(input())
# answer = 0
# a = 0
# i = 1
#
# while n != 0:
#     if i > n :
#         i = 1
#     elif i == n:
#         answer += 1
#         break
#     else:
#         answer += 1
#         n -= i
#         i += 1
#
# print(answer)

# n = int(input())
# answer = []
#
# for i in range(n):  answer.append(int(input()))
#
# max = answer[0]
# max2 = answer[-1]
# a = 1
# b = 1
#
# for i in answer[1:]:
#     if i > max:
#         a += 1
#         max = i
#
# for i in answer[::-1][1:]:
#     if i > max2:
#         b += 1
#         max2 = i
#
#
# print(a)
# print(b)

# for i in range(10):
#     print('asd')

# n = int(input())
# a = [1,2,3]
# count = 3
# if n <= 3:
#     print(a[n-1])
# else:
#     while len(a) != n:
#         a.append((a[-3]+2*a[-2])%15746)
#     print(a[-1])

# n = int(input())
# arr = list(map(int,input().split()))
# answer = []
#
# for i in range(len(arr)):
#     target = [k for k in range(len(arr[:i])) if arr[k] < arr[i]]
#     if target != []:
#         answer.append(max([answer[i] for i in target])+1)
#     else:
#         answer.append(1)
# print(max(answer))

# from collections import deque
#
# N,S,M = map(int,input().split())
# volume = list(map(int,input().split()))
# possible = deque([[]])
#
# if M >= S - volume[0] >= 0: possible[0].append(S - volume[0])
# if M >= S + volume[0] >= 0: possible[0].append(S + volume[0])
#
# a = True
# for i in range(1,N):
#     added = []
#     for j in possible[0]:
#         if M >= j + volume[i] >= 0 and j + volume[i] not in added :
#             added.append(j + volume[i])
#         if M >= j - volume[i] >= 0 and j - volume[i] not in added:
#             added.append(j - volume[i])
#     if added == []: break
#     possible.popleft()
#     possible.append(added)
# else:
#     if possible[0] != []:
#         print(max(possible[0]))
#     else:
#         print(-1)
#     a = False
# if a:
#     print(-1)


# 로또의 최고 순위와 최저 순위
# def solution(lottos, win_nums):
#     count = 0
#     zeroCount = 0
#     for i in lottos:
#         if i in win_nums: count += 1
#         elif i == 0: zeroCount += 1
#     if count == 0:
#         if zeroCount <= 1: return [6, 6]
#         else: return [6-zeroCount+1, 6]
#     elif count == 1:
#         if zeroCount == 0: return [6, 6]
#         else: return [6-zeroCount, 6]
#
#     else:
#         return [6-zeroCount-count+1, 6-count+1]

#1018 체스판
# n,m = map(int,input().split())
#
# total = []
# answers = []
#
# def turnOne(total,i,j,mode):
#     a = [['B','W'],['W','B']]
#     answer = 0
#     for k in range(8):
#         for u in range(8):
#             if (k+u)%2 == 1 and total[i+k][j+u] != a[mode][0]:
#                 answer += 1
#             elif (k+u)%2 == 0 and total[i+k][j+u] != a[mode][1]:
#                 answer += 1
#
#     return answer
#
# for i in range(n):
#     total.append(list(input()))
#
# for i in range(n-7):
#     for j in range(m-7):
#         answers.append(turnOne(total,i,j,0))
#         answers.append(turnOne(total,i,j,1))
#
# print(min(answers))


# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if signs[i] == False:
#             answer -= absolutes[i]
#         else:
#             answer += absolutes[i]
#     return answer

# from collections import deque
#
# totalCount, targetCount = map(int,input().split())
#
# targets = list(map(int,input().split()))
# total = deque([i for i in range(1,totalCount+1)])
# [1,2,3,4,5]
#
# answer = 0
#

# 회전하는 큐(1021)
# for i in targets:
#     frontCount = 0
#     for k in total:
#         if k == i:
#             break
#         else:
#             frontCount += 1
#     backCount = len(total)-frontCount
#     if frontCount < backCount:
#         while total[0] != i:
#             total.append(total.popleft())
#             answer += 1
#     else:
#         while total[0] != i:
#             total.appendleft(total.pop())
#             answer += 1
#     total.popleft()
# print(answer)


# 분수찾기 (브론즈1) 1193번
# n = int(input())
# k = 0
# while (k*(k+1))/2 <= n:
#     k += 1
# under = k-1
#
# i = 0
# while k*(k-1)/2 + i != n:
#     i += 1
#
# if (i == 0):
#     if (((k-1) % 2) == 0):
#         print(k - 1, '/', 1, sep='')
#     else:
#         print(1, '/', k - 1, sep='')
# else:
#     if (((k - 1) % 2) == 0):
#         print(k - i + 1, '/', i, sep='')
#     else:
#         print(i, '/', k + 1 - i, sep='')

# 소트인사이드 (실버5) 1427번

# total = list(map(int,list(input())))
# total = sorted(total,reverse=True)
# print(''.join(map(str,total)))


# 늑대와 양 (실버3) 16956번
# from collections import deque
#
# r,c = map(int,input().split())
# total = []
#
# for i in range(r):
#     total.append(list(input()))
#
# q = deque([])
# for i in range(r):
#     for j in range(c):
#         if total[i][j] == '.':
#             total[i][j] = 'D'
#         if total[i][j] == 'W':
#             q.append([i,j])
#
# possible = 1
# while q:
#     i,j = q.popleft()
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     for k in range(4):
#         if 0 <= i+dx[k] < r and 0 <= j+dy[k] < c and (total[i+dx[k]][j+dy[k]] == 'S'):
#             possible = 0
#
# if possible == 1:
#     print(possible)
#     for i in total:
#         print(''.join(i))
# else:
#     print(possible)


# 알파벳
# from collections import deque

# r,c = map(int,input().split())
# total = []
# for i in range(r):
#     total.append(list(input()))
# answer = 0
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# newAcc = [total[0][0]]
#
# def check():
#     global answer
#     q = set()
#     q.add((0,0,total[0][0]))
#     while q:
#         x,y,route = q.pop()
#         if len(route) > answer :
#             answer = len(route)
#
#         for i in range(4):
#             if 0 <= x+dx[i] < r and 0 <= y+dy[i] < c:
#                 if total[x+dx[i]][y+dy[i]] not in route:
#                     q.add((x+dx[i], y+dy[i], route + total[x+dx[i]][y+dy[i]]))
# check()
# print(answer)

# 주사위 4개 브론즈2 2484번
# n =  int(input())
# total = []
# for i in range(n):
#     total.append(list(map(int,input().split())))
# answer = []
#
# def countSameNumber(arr):
#     a = [0,0]
#     for i in arr:
#         if arr.count(i) > a[1]:
#             a = [i,arr.count(i)]
#     return a
#
# for i in total:
#     setedList = set(i)
#     if len(setedList) == 1:
#         answer.append(50000 + list(setedList)[0]*5000)
#     elif len(setedList) == 2 and countSameNumber(i)[1] == 3:
#         answer.append(10000 + countSameNumber(i)[0] * 1000)
#     elif len(setedList) == 2 and countSameNumber(i)[1] == 2:
#         answer.append(2000 +  list(setedList)[0] * 500 +  list(setedList)[1] * 500)
#     elif len(setedList) == 3:
#         answer.append(1000 + countSameNumber(i)[0] * 100)
#     elif len(setedList) == 4 :
#         answer.append(max(setedList)*100)
# print(max(answer))

# 꽃길 실버2 14620번
# from itertools import combinations
#
# n = int(input())
# total = []
# for i in range(n):
#     total.append(list(map(int,input().split())))
# answer = []
# target = []
#
# def possible(arr):
#     z = []
#     dx = [-1, 0, 1, 0, 0]
#     dy = [0, 1, 0, -1, 0]
#     for i in arr:
#         for a in range(5):
#             z.append((i[0]+dx[a],i[1]+dy[a]))
#     if(len(set(z)) == len(z)):
#         return sum([total[i[0]][i[1]] for i in z])
#     return -1
#
# for i in range(1,n-1):
#     for j in range(1,n-1):
#         target.append([i,j])
#

# for i in list(combinations(target,3)):
#     possi = possible(i)
#     if (possi != -1): answer.append(possi)
#
# print(min(answer))

# 생일 5635 실버 5
# n = int(input())
# total = []
# for i in range(n):
#     a = list(input().split())
#     a[1] = int(a[1])
#     a[2] = int(a[2])
#     a[3] = int(a[3])
#     total.append(list(reversed(a)))
# total = sorted(total)
# print(total[-1][3])
# print(total[0][3])



# 나이트의 이동 7562번 실버2
# from collections import deque
#
# n = int(input())
#
# for i in range(n):
#     a = int(input())
#     total = [[False for k in range(a)] for j in range(a)]
#     now = list(map(int,input().split()))
#     target = list(map(int, input().split()))
#     q = deque([])
#     q.append([now[0],now[1],0])
#     total[now[0]][now[1]] = True
#     direction = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]
#
#     while q:
#         x,y,count = q.popleft()
#         if [x, y] == target:
#             print(count)
#             break
#
#         for i in direction:
#             if 0 <= x + i[0] < a and 0 <= y + i[1] < a and total[x + i[0]][y + i[1]] == False:
#                 total[x + i[0]][y + i[1]] = True
#                 q.append([x + i[0],y + i[1],count+1])

# 다이얼 브론즈2 5622
# total = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = list(input())
# number = []
# for i in word:
#     for j in range(len(total)):
#         if i in total[j]:
#             number.append(2+j)
# print(sum(number)+len(number))

# 정수 N개의 합 브론즈2 15596

# def solve(list):
#     a = 0
#     for i in list:
#         a += i
#     return a

# 빠른 A + B 브론즈2 15552
# import sys
# input = sys.stdin.readline
# n = int(input())
# for i in range(n):
#     a,b = list(map(int,input().split()))
#     print(a+b)

# 네 번째 점 브론즈3 3009
# a = []
# b = []
#
# def find(arr):
#     for i in arr:
#         if arr.count(i) != 2:
#             return i
# for i in range(3):
#     x,y = list(map(int,input().split()))
#     a.append(x)
#     b.append(y)
# print(find(a), find(b))

# 팩토리얼 브론즈3 10872
# n = int(input())
# a = 1
# for i in range(n,0,-1):
#     a = a * i
# print(a)

# 피보나치 수 5 브론즈2 10870
# n = int(input())
#
# ans = [0,1,1]
# if n >= 3:
#     for i in range(n-2):
#         ans.append(ans[-1]+ans[-2])
# print(ans[n])

# 수 정렬하기 브론즈1 2750번
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr = sorted(arr)
# for i in arr:
#     print(i)

# 최소공배수 실버5 1934번
# from math import gcd
# n = int(input())
# for i in range(n):
#     a,b = map(int,input().split())
#     print(a*b//gcd(a,b))

# 이름 궁합 브론즈2 15312번
# x = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
# a = [x[i-65] for i in list(map(ord,list(input())))]
# b = [x[i-65] for i in list(map(ord,list(input())))]
# answer = []
# for i in range(len(a)):
#     answer.append(a[i])
#     answer.append(b[i])
# while len(answer) != 2:
#     new = []
#     for i in range(len(answer)-1):
#         new.append((answer[i] + answer[i+1])%10)
#     answer = new
# print(''.join(map(str,answer)))

# 문자열 실버4 1120번
# a,b = input().split()
# target = len(b) - len(a)
# answers = []
# for i in range(target+1):
#     count = 0
#     for index,v in enumerate(b[i:i+len(a)]):
#         if a[index] != v:
#             count += 1
#     answers.append(count)
# print(min(answers))

# 회문 실버1 17609번
# def pelim(a,last):
#     for i in range(len(a)//2):
#         if a[i] != a[len(a)-1-i]:
#             if last == False:
#                 if 0 in [pelim(a[:i]+a[i+1:],True),pelim(a[:len(a)-1-i]+a[len(a)-i:],True)]:
#                     return 1
#                 else:
#                     return 2
#             else:
#                 return 2
#     else: return 0
# n = int(input())
# total = []
# answer = []
# for i in range(n): total.append(input())
# for i in total: answer.append(pelim(i,False))
# for i in answer: print(i)

#고층건물 골드4 1027번
# n = int(input())
# total = list(map(int,input().split()))
# answer = []
# for i,v in enumerate(total):
#     count = 0
#     for i2,v2 in enumerate(total):
#         per = 0
#         if i > i2:
#             gap = v2 - v
#             for k in range(1,i-i2+1):
#                 if v + gap * (k/(i-i2)) <= total[i-k]:
#                     per += 1
#             if per == 1:
#                 count += 1
#         elif i < i2:
#             gap = v2 - v
#             for k in range(1, i2-i+1):
#                 if v + gap * (k / (i2 - i)) <= total[i+k]:
#                     per += 1
#             if per == 1:
#                 count += 1
#     answer.append(count)
#
# print(max(answer))

# 영역 구하기 실버1 2583번
# import sys
# sys.setrecursionlimit(10000)
#
# y,x,c = map(int,input().split())
# total = []
# for i in range(y):
#     total.append([False for j in range(x)])
#
# target = []
# for i in range(c):
#     target.append(list(map(int,input().split())))
#
# for x1,y1,x2,y2 in target:
#     for i in range(y2,y1,-1):
#         for j in range(x1,x2):
#             total[y-i][j] = True
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# count = 0
# land = 0
# answer = []
#
# def dfs(l,m):
#     global count
#     total[l][m] = True
#     count += 1
#     for i in range(4):
#         if y > l + dx[i] >= 0 and x > m + dy[i] >= 0 and total[l + dx[i]][m + dy[i]] == False:
#             dfs(l + dx[i], m + dy[i])
#
# for i in range(y):
#     for j in range(x):
#         if total[i][j] == False:
#             land += 1
#             dfs(i,j)
#             answer.append(count)
#             count = 0
# print(land)
# print(' '.join(map(str,sorted(answer))))


# 암호만들기 골드5 1759
# n,m = map(int,input().split())
# total = sorted(list(input().replace(' ','')))
# answer = []
# target = set(['a','e','i','o','u'])
# def check(now,index):
#     if len(now) == n:
#         inter = len(set(list(now)).intersection(target))
#         if inter >= 1 and len(now) - inter >= 2:
#             return answer.append(now)
#         else:
#             return
#     if len(now) + m-(index+1) < n: return
#     for i in range(index+1,m):
#         check(now+total[i],i)
# for i,v in enumerate(total):
#     check(v,i)
# for i in answer:
#     print(i)

# 배 골드5 1092
# n = int(input())
# crain = sorted(list(map(int,input().split())),reverse=True)
# m = int(input())
# box = sorted(list(map(int,input().split())),reverse=True)
#
# count = 0
# if box[0] > crain[0]: print(-1)
# else:
#     while box:
#         count += 1
#         for i in crain:
#             if len(box) == 0 : break
#             for j,v in enumerate(box):
#                 if i >= v:
#                     del box[j]
#                     break
#  print(count)

# 특정거리의 도시 찾기 실버2 18352번
# import heapq
#
# n,m,k,x = map(int,input().split())
# total = {}
# INF = int(1e9)
# distance = [INF for i in range(n+1)]
# for i in range(m):
#     frm,to = map(int,input().split())
#     if frm in total.keys():
#         total[frm].append(to)
#     else:
#         total[frm] = [to]
#
# q = []
# heapq.heappush(q,(0,x))
# distance[x] = 0
#
# while q:
#     cost,now = heapq.heappop(q)
#     # 돌아서 온경우구나!
#     if distance[now] < cost:
#         continue
#     else:
#         if now not in total.keys(): continue
#
#         for i in total[now]:
#             if distance[i] > cost + 1:
#                 distance[i] = cost+1
#                 heapq.heappush(q,(cost+1,i))
# if k not in distance:
#     print(-1)
# else:
#     for i,v in enumerate(distance):
#         if v == k:
#             print(i)

# 미로 골드4 2665번
# import heapq
#
# n = int(input())
# total = []
# target = []
# INF = int(1e9)
#
# for i in range(n):
#     total.append(list(map(int,list(input()))))
#     target.append([INF for i in range(n)])
# q = []
# heapq.heappush(q,(0,[0,0]))
# target[0][0] = 0
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# while q:
#     cost, now = heapq.heappop(q)
#     if now == (n-1,n-1):
#         print(cost)
#         break
#     for i in range(4):
#         if n > now[0] + dx[i] >= 0 and n > now[1] + dy[i] >= 0:
#             if total[now[0] + dx[i]][now[1] + dy[i]] == 0:
#                 if target[now[0] + dx[i]][now[1] + dy[i]] > cost+1:
#                     target[now[0] + dx[i]][now[1] + dy[i]] = cost + 1
#                     heapq.heappush(q,(cost+1,(now[0] + dx[i],now[1] + dy[i])))
#             else:
#                 if target[now[0] + dx[i]][now[1] + dy[i]] > cost:
#                     target[now[0] + dx[i]][now[1] + dy[i]] = cost
#                     heapq.heappush(q, (cost, (now[0] + dx[i], now[1] + dy[i])))

# 표 편집 프로그래머스 3단계 카카오 기출
# def cal(answer,v,number,up):
#     count = 0
#     real = 0
#     if up == True:
#         while real != number:
#             if answer[v-(count+1)] == 'O': real += 1
#             count += 1
#         return v-count
#     else:
#         while real != number:
#             if answer[v+(count+1)] == 'O':
#                 real += 1
#             count += 1
#         return v+count
#
# def moveup(answer,now):
#     count = 1
#     while answer[now-count] == 'X':
#         count += 1
#     return now-count
#
# def movedown(answer,now):
#     count = 1
#     while answer[now+count] == 'X':
#         count += 1
#     return now+count
#
# def solution(n, k, cmd):
#     answer = ['O' for i in range(n)]
#     now = k
#     trash = []
#     for order in cmd:
#         if len(order) > 1:
#             direction, count = order.split()
#             if direction == 'U':
#                 now = cal(answer,now,int(count),True)
#             else:
#                 now = cal(answer,now,int(count),False)
#         else:
#             if order == 'C':
#                 trash.append(now)
#                 answer[now] = 'X'
#                 if now == len(answer)-1:
#                     now = moveup(answer,now)
#                 else:
#                     now = movedown(answer,now)
#             else:
#                 re = trash.pop()
#                 answer[re] = 'O'
#         print(answer, now,order)
#     return ''.join(answer)
# print(solution(8,2,["U 2","C","C","Z","Z",]))
# print(solution(8,2,["C","C","C","C","C",'U 1','C','U 1','D 1','C','Z','Z','Z','Z','D 4']))

# 먹을 것인가 먹힐 것인가 실버3 7795번
# from bisect import bisect_left
#
# n = int(input())
# for i in range(n):
#     a,b = map(int,input().split())
#     Aarr = list(map(int,input().split()))
#     Barr = sorted(list(map(int, input().split())))
#     answer = 0
#     for i in Aarr:
#         answer += bisect_left(Barr,i)
#     print(answer)

# 미로탈출 프로그래머스 4단계 카카오 기출
# import heapq
#
# def solution(n, start, end, roads, traps):
#     dic = {i+1:[] for i in range(n)}
#     reverseDic = {i+1:[] for i in range(n)}
#     INF = int(1e9)
#     distance = [INF for _ in range(n+1)]
#     visitedCount = [0 for _ in range(n+1)]
#     for frm,to,cost in roads:
#         dic[frm].append((cost,to))
#         reverseDic[to].append((cost,frm))
#     q = []
#     heapq.heappush(q,(0,start,dix))
#     distance[start] = 0
#     while q:
#         cost,now = heapq.heappop(q)
#         visitedCount[now] += 1
#         if now == end :
#             print(now,'asd')
#         if now in traps:
#             if visitedCount[now] == 1:
#                 for added, to in reverseDic[now]:
#                     distance[to] = cost + added
#                     heapq.heappush(q,(cost + added,to))
#             elif visitedCount[to] == 2:
#                 for added, to in dic[now]:
#                     distance[to] = cost + added
#                     heapq.heappush(q,(cost + added,to))
#         else:
#             for added,to in dic[now]:
#                 if distance[to] > cost + added:
#                     distance[to] = cost + added
#                     heapq.heappush(q,(cost + added,to))
#         print(distance)
#     return distance[end]
#
# # print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))

# 연산자 끼워넣기 실버1 14888
# n = int(input())
# numbers = list(map(int,input().split()))
# operation = list(map(int,input().split()))
# answers = []
#
# def cal(num,oper,count):
#     if oper == [0,0,0,0]:
#         answers.append(num)
#     for i,v in enumerate(oper):
#         if v == 0: continue
#         if i == 0:
#             newOper = [z for z in oper]
#             newOper[i] -= 1
#             cal(num+numbers[count+1],newOper,count+1)
#         elif i == 1:
#             newOper = [z for z in oper]
#             newOper[i] -= 1
#             cal(num-numbers[count+1],newOper,count+1)
#         elif i == 2:
#             newOper = [z for z in oper]
#             newOper[i] -= 1
#             cal(num*numbers[count+1],newOper,count+1)
#         elif i == 3:
#             newOper = [z for z in oper]
#             newOper[i] -= 1
#             if num < 0:
#                 cal(-((-num)//numbers[count+1]),newOper,count+1)
#             else:
#                 cal(num//numbers[count+1],newOper,count+1)
#
# cal(numbers[0],operation,0)
# print(max(answers))
# print(min(answers))

# 가장 먼 노드 프로그래머스 LV3
# import heapq
#
# def solution(n, edge):
#     dic = {i+1:[] for i in range(n)}
#     INF = int(1e9)
#     distance = [INF for i in range(n+1)]
#     for frm,to in edge:
#         dic[frm].append(to)
#         dic[to].append(frm)
#     q = []
#     heapq.heappush(q,(0,1))
#     distance[1] = 0
#     while q:
#         cost,now = heapq.heappop(q)
#         for to in dic[now]:
#             if distance[to] > cost + 1:
#                 distance[to] = cost + 1
#                 heapq.heappush(q,(cost+1,to))
#     distance = sorted(distance,reverse=True)
#     maxi = 0
#     for i in distance:
#         if i != INF:
#             maxi = i
#             break
#     answer = 0
#     for i in distance:
#         if i == maxi:
#             answer += 1
#     return answer

# 멀리뛰기기
# def solution(n):
#     arr = [0 for i in range(n)]
#     arr[0] = 1
#     if n > 1:
#         arr[1] = 2
#         for i in range(2,n):
#             arr[i] = arr[i-1] + arr[i-2]
#     return arr[-1] % 1234567
# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))

# 다리 놓기 실버5
# n = int(input())
# for i in range(n):
#     a,b = map(int,input().split())
#     under = 1
#     up = 1
#     for i in range(1,a+1):
#         up *= b-(i-1)
#         under *= i
#     print(up//under)

# 주유소 실버4 13305번
# n = int(input())
# line = list(map(int,input().split()))
# node = list(map(int,input().split()))
# answer = 0
# price = 0
# for i,v in enumerate(node):
#     if i == len(node)-1:break
#     if i == 0:
#         price = v
#         answer += price*line[i]
#     elif price <= v:
#         answer += price*line[i]
#     elif price > v:
#         price = v
#         answer += price * line[i]
# print(answer)

# 아이템 줍기 프로그래머스 LV3
# from collections import deque
#
# def solution(rectangle, characterX, characterY, itemX, itemY):
#     total = [[-1 for j in range(50)] for i in range(50)]
#     visited = [[False for j in range(50)] for i in range(50)]
#     last = [[False for j in range(50)] for i in range(50)]
#     for x1,y1,x2,y2 in rectangle:
#         for y in range(y1,y2+1):
#             for x in range(x1,x2+1):
#                 if visited[49-y][x] == False:
#                     visited[49-y][x] = True
#                     if x in [x1,x2] or 49-y in [49-y1,49-y2]:
#                         total[49-y][x] = 0
#                     else:
#                         total[49-y][x] = 1
#                 else:
#                     if x in [x1, x2] or 49-y in [49-y1, 49-y2]:
#                         total[49-y][x] += 0
#                     else:
#                         total[49-y][x] += 1
#
#     answer = 0
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     a = []
#     q = deque([])
#     a.append((characterY,characterX))
#     last[49-characterY][characterX] = True
#
#     for i in range(4):
#         if 0 <= 49-(characterY+dy[i]) < 50 and 0 <= characterX+dx[i] < 50:
#             if total[49-(characterY+dy[i])][characterX+dx[i]] == 0:
#                 last[49-(characterY+dy[i])][characterX+dx[i]] = True
#                 a.append((characterY+dy[i],characterX+dx[i]))
#                 q.append((characterY+dy[i],characterX+dx[i]))
#                 break
#     while q:
#         cY,cX = q.popleft()
#         for i in range(4):
#             if 0 <= cY+dy[i] < 50 and 0 <= cX+dx[i] < 50:
#                 if total[49-(cY+dy[i])][cX+dx[i]] == 0 and last[49-(cY+dy[i])][cX+dx[i]] is False:
#                     last[49-(cY+dy[i])][cX+dx[i]] = True
#                     a.append((cY+dy[i],cX+dx[i]))
#                     q.append((cY+dy[i],cX+dx[i]))
#                     break
#     targetIndex = 0
#     for i,v in enumerate(a):
#         if v == (itemY,itemX):
#             targetIndex = i
#     if targetIndex > len(a) - targetIndex:
#         return len(a) - targetIndex
#     else:
#         return targetIndex
#
# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],9,7,6,1))
# print(solution([[1,1,5,7]],1,1,4,7))
# print(solution([[2,1,7,5],[6,4,10,10]],3,1,7,10))
# print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],1,4,6,3))

# 백대열 실버4 14490
# from math import gcd
# a,b = map(int,input().split(':'))
# gd = gcd(a,b)
# print(a//gd,':',b//gd,sep='')

# def solution(N, trust):
#     total = [i+1 for i in range(N)]
#     for i in trust:
#       if i[0] in total:
#         total.remove(i[0])
#     trusted = [i[1] for i in trust]
#     for i in trusted:
#       if trusted.count(i) != N-1 and i in total:
#         total.remove(i)
#     if len(total) > 1 or len(total) == 0:
#       return -1
#     return total[0]

# 피로도 프로그래머스LV2
# from itertools import permutations
#
# def solution(k, dungeons):
#     length = len(dungeons)
#     total = list(permutations(dungeons,length))
#     answers = []
#     for one in total:
#         pi = k
#         answer = 0
#         for i in one:
#             if pi >= i[0]:
#                 pi -= i[1]
#                 answer += 1
#         answers.append(answer)
#     return max(answers)
#
# print(solution(80,[[80,20],[50,40],[30,10]]))

# 안전영역 2428번 실버1
# from collections import deque
# n = int(input())
# total = []
# flatedTotal = []
# for i in range(n):
#     a = list(map(int,input().split()))
#     total.append(a)
#     for z in a:
#         flatedTotal.append(z)
# maxi = max(flatedTotal)
# mini = min(flatedTotal)
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# answer = []
# for i in range(0, 101):
#     visited = [[False for _ in one] for one in total]
#     miniAnswer = 0
#     for x in range(n):
#         for y in range(n):
#             if total[x][y] > i and visited[x][y] is False:
#                 q = deque([])
#                 q.append([x,y])
#                 miniAnswer += 1
#                 visited[x][y] = True
#                 while q:
#                     X,Y = q.popleft()
#                     for v in range(4):
#                         if 0 <= X+dx[v] < n and 0 <= Y+dy[v] < n:
#                             if total[X+dx[v]][Y+dy[v]] > i and visited[X+dx[v]][Y+dy[v]] is False:
#                                 q.append([X+dx[v],Y+dy[v]])
#                                 visited[X][Y] = True
#     answer.append(miniAnswer)
# print(max(answer))

#토마토 7576번 실버1
# n,l = map(int,input().split())
# total = []
# q = []
# for i in range(l): total.append(list(map(int,input().split())))
#
# for i in range(l):
#     for j in range(n):
#         if total[i][j] == 1:
#             q.append([i,j])
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# answer = -1
# while q:
#     answer += 1
#     newQ = []
#     for i,j in q:
#         for z in range(4):
#             if 0 <= i+dx[z] < l and 0 <= j+dy[z] < n and total[i+dx[z]][j+dy[z]] == 0:
#                 newQ.append([i+dx[z], j+dy[z]])
#                 total[i+dx[z]][j+dy[z]] = 1
#     q = newQ
# zz = 0
# for i in total:
#     for j in i:
#         if j == 0:
#             zz = -1
# if zz == -1:
#     print(-1)
# else:
#     print(answer)

# 연속합 1912번 실버2
# n = int(input())
# total = list(map(int,input().split()))
# cash = []
# cash.append(total[0])
# for i in range(1,len(total)):
#     cash.append(max(0,cash[i-1])+total[i])
# print(max(cash))

# 효율적인 해킹 실버1
# from collections import deque
#
# n,m = map(int,input().split())
# dic = {i:[] for i in range(1,n+1)}
# visited = [False for i in range(0,n+1)]
# for i in range(m):
#     to,frm = map(int,input().split())
#     dic[frm].append(to)
#
# answers = []
# for i in range(1,n+1):
#     q = deque([])
#     q.append(i)
#     visited = [False for i in range(0, n + 1)]
#     visited[i] = True
#     miniAnswer = 1
#     while q:
#         now = q.popleft()
#         for i in dic[now]:
#             if visited[i] is False:
#                 visited[i] = True
#                 q.append(i)
#                 miniAnswer += 1
#     answers.append(miniAnswer)
# maxi = max(answers)
# for i,v in enumerate(answers):
#     if v == maxi:
#         print(i+1 ,sep=' ')

# 전쟁-전투 실버1 1303번
# from collections import deque
#
# m,l = map(int,input().split())
# total = []
# visited = []
# for i in range(l):
#     oneLine = list(input())
#     total.append(oneLine)
#     visited.append([False for i in range(len(oneLine))])
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# answer = [0,0]
# for i in range(l):
#     for j in range(m):
#         if visited[i][j] is True: continue
#         q = deque([])
#         q.append([i,j])
#         visited[i][j] = True
#         miniAnswer = 1
#         while q:
#             x,y = q.popleft()
#             for z in range(4):
#                 if 0 <= x+dx[z] < l and 0 <= y+dy[z] < m and visited[x+dx[z]][y+dy[z]] is False:
#                     if total[x+dx[z]][y+dy[z]] == total[x][y]:
#                         q.append([x+dx[z],y+dy[z]])
#                         miniAnswer += 1
#                         visited[x + dx[z]][y + dy[z]] = True
#         if total[i][j] == 'W':
#             answer[0] += miniAnswer * miniAnswer
#         else:
#             answer[1] += miniAnswer * miniAnswer
# print(' '.join(map(str,answer)))

# 예산 2512번 실버3
# n = int(input())
# prices = list(map(int,input().split()))
# total = int(input())
# start = 0
# end = max(prices)
# answer = 0
# def isPossible(price):
#     mi = 0
#     for i in prices:
#         if i <= price:
#             mi += i
#         else:
#             mi += price
#     if mi <= total:
#         return price
#     return False
#
# while start <= end:
#     pivot = (start + end) // 2
#     if isPossible(pivot):
#         answer = isPossible(pivot)
#         start = pivot + 1
#     else:
#         end = pivot - 1
#
# print(answer)

# 포도주 시식 2156번 실버1
# n = int(input())
# total = []
# for i in range(n):
#     total.append(int(input()))
# answers = []
# if len(total) == 1:
#     print(total[0])
# elif len(total) == 2:
#     print(total[0] + total[1])
# else:
#     answers = [total[0], total[0] + total[1], max([total[0] + total[1],total[0] + total[2],total[2] + total[1]])]
#     for i in range(3,n):
#         answers.append(max(answers[i-2]+total[i], answers[i-3]+total[i-1]+total[i], answers[i-1]))
#     print(max(answers))

# 물통 실버1 2251번
# from collections import deque
#
# a,b,c = map(int,input().split())
# total = [a,b,c]
# answers = set()
# q = deque([])
# visited = set()
# q.append((0,0,c))
# while q:
#     list1 = q.popleft()
#     A,B,C = list1
#     if list1 in visited: continue
#     visited.add(list1)
#     if list1[0] == 0 :answers.add(C)
#     if list1[0] <= b - list1[1]: q.append((0, list1[1] + list1[0], list1[2]))
#     else: q.append(((list1[0] + list1[1]) - b, b, list1[2]))
#
#     if list1[0] <= c - list1[2]: q.append((0, list1[1], list1[2] + list1[0]))
#     else: q.append((list1[0] + list1[2] - c, list1[1], c))
#
#     if list1[1] <= a - list1[0]: q.append((list1[0] + list1[1], 0, list1[2]))
#     else: q.append((a, list1[1] + list1[0] - a, list1[2]))
#
#     if list1[1] <= c - list1[2]: q.append((list1[0], 0, list1[1] + list1[2]))
#     else: q.append((list1[0], list1[1] + list1[2] - c, c))
#
#     if list1[2] <= a - list1[0]: q.append((list1[0] + list1[2], list1[1], 0))
#     else: q.append((a, list1[1], list1[0] + list1[2] - a))
#
#     if list1[2] <= b - list1[1]: q.append((list1[0], list1[1] + list1[2], 0))
#     else: q.append((list1[0], b, list1[1] + list1[2] - b))
#
# print(' '.join(map(str,sorted((answers)))))

# 이분 그래프 골드4 1707번
# from collections import deque
#
# k = int(input())
# for i in range(k):
#     v,e = map(int,input().split())
#     dic = {i+1:[] for i in range(v)}
#     visited = [False for i in range(v)]
#     for j in range(e):
#         a,b = map(int,i
#         print('YES')nput().split())
#         dic[a].append(b)
#         dic[b].append(a)
#     miniAnswer = 0
#     isPossible = True
#     for s in range(1,v+1):
#         if visited[s-1] is not False: continue
#         miniAnswer += 1
#         q = deque([s])
#         visited[s-1] = 'WHITE'
#         while q:
#             now = q.popleft()
#             if not isPossible:
#                 break
#             for a in dic[now]:
#                 if visited[a-1] is False:
#                     q.append(a)
#                     if visited[now-1] == 'WHITE':
#                         visited[a-1] = 'BLACK'
#                     else: visited[a-1] = 'WHITE'
#                 else:
#                     if visited[a-1] == visited[now-1]:
#                         isPossible = False
#         if not isPossible:
#             break
#     if not isPossible:
#         print('NO')
#     else:

# def solution(n, computers):
#     copyedComputers = [computer[:] for computer in computers]
#     answer = 0
#
#     def dfs(i):
#         for j in range(n):
#             if copyedComputers[i][j] == 1:
#                 copyedComputers[i][j] = 2
#                 dfs(j)
#
#     for i in range(n):
#         if 1 in copyedComputers[i]:
#             answer += 1
#             dfs(i)
#
#     return answer
#
# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# 1085 직사각형에서 탈출

# x,y,w,h = map(int,input().split())
# print(min(x,y,w-x,h-y))


#1018 체스판
# n,m = map(int,input().split())
#
# total = []
# answers = []
#
# def turnOne(total,i,j,mode):
#     a = [['B','W'],['W','B']]
#     answer = 0
#     for k in range(8):
#         for u in range(8):
#             if (k+u)%2 == 1 and total[i+k][j+u] != a[mode][0]:
#                 answer += 1
#             elif (k+u)%2 == 0 and total[i+k][j+u] != a[mode][1]:
#                 answer += 1
#
#     return answer
#
# for i in range(n):
#     total.append(list(input()))
#
# for i in range(n-7):
#     for j in range(m-7):
#         answers.append(turnOne(total,i,j,0))
#         answers.append(turnOne(total,i,j,1))
#
# print(min(answers))

# 1259 팰린드롬수

# answer = []
#
# while True:
#     n = input()
#     if not int(n): break
#     if len(n)%2 == 1 and list(n)[:len(n)//2][::-1] == list(n)[len(n)//2+1:]:
#         print('yes')
#         continue
#     if len(n)%2 == 0 and list(str(n))[:len(n)//2][::-1] == list(str(n))[len(n)//2:]:
#         print('yes')
#         continue
#     print('no')

# 1181번 정렬

# n = int(input())
# total = []
# for i in range(n):
#     word = input()
#     total.append((len(word),word))
# total = sorted(list(set(total)))
#
# for i in total:
#     print(i[1])

#1018 체스판
# n,m = map(int,input().split())
#
# total = []
# answers = []
#
# def turnOne(total,i,j,mode):
#     a = [['B','W'],['W','B']]
#     answer = 0
#     for k in range(8):
#         for u in range(8):
#             if (k+u)%2 == 1 and total[i+k][j+u] != a[mode][0]:
#                 answer += 1
#             elif (k+u)%2 == 0 and total[i+k][j+u] != a[mode][1]:
#                 answer += 1
#
#     return answer
#
# for i in range(n):
#     total.append(list(input()))
#
# for i in range(n-7):
#     for j in range(m-7):
#         answers.append(turnOne(total,i,j,0))
#         answers.append(turnOne(total,i,j,1))
#
# print(min(answers))

# from itertools import permutations
#
# def solution(expression):
#     number = []
#     pri = []
#     buket = []
#
#     answer = []
#     for i in expression:
#         if i in ['*','+','-']:
#             number.append(int(''.join(buket)))
#             buket = []
#             pri.append(i)
#         else:
#             buket.append(i)
#     number.append(int(''.join(buket)))
#
#     print(number, pri, buket)
#     for oper in permutations(['*','+','-'],3):
#         count = 'start'
#         for op in oper:
#             for index in range(len(pri)):
#                 if pri[index] == op:
#                     if count == 'start':
#                         count = number[index]
#                     if op == '*':
#                         count *= number[index + 1]
#                     elif op == '+':
#                         count += number[index + 1]
#                     else:
#                         count -=  number[index + 1]
#
#         answer.append(abs(count))
#
#     return max(answer)

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

# def tilt(s):
#     length = len(s)
#     answer = [[0 for i in range(length)] for j in range(length)]
#
#     for i in range(length):
#         for j in range(length):
#             answer[j][length-1-i] = s[i][j]
#     return answer

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

 # import heapq
#
# nodes,lines = list(map(int,input().split(' ')))
# fro = int(input())
#
# INF = int(1e9)
# answers = [INF for i in range(nodes+1)]
# visited = [False for i in range(nodes+1)]
#
# kings = []
# heapq.heappush(kings,(0, fro))
# infoArr = [[] for _ in range(nodes+1)]
#
# for i in range(lines):
#     start, end, time = list(map(int, input().split(' ')))
#     infoArr[start].append([end,time])
#
# while kings:
#     answer, index = heapq.heappop(kings)
#     if visited[index]:
#         continue
#     visited[index] = True
#     answers[index] = answer
#
#     for end, time in infoArr[index]:
#         if answers[end] > answer + time:
#             answers[end] = answer + time
#             heapq.heappush(kings,(answer + time, end))
#
# for i in range(1,len(answers)):
#     print(answers[i])

# 숫자카드게임
# row,col = map(int,input().split())
# resultCompare = []
# squre = [[0]*col for i in range(row)]
# for i in range(row):
#     squre[i] = list(map(int,input().split()))
#
# for i in range(row):
#     squre[i].sort()
#     resultCompare.append(squre[i][0])
#
# print(sorted(resultCompare)[-1])

# import sys
#
# n = int(input())
#
# for i in range(n):
#     inputs = list(sys.stdin.readline().rstrip())
#     answerLeft = []
#     answerRight = []
#     cursor = 0
#     for i in inputs:
#         if i == '<':
#             if answerLeft != []:
#                 answerRight.append(answerLeft.pop())
#         elif i == '>':
#             if answerRight != []:
#                 answerLeft.append(answerRight.pop())
#         elif i == '-':
#             if answerLeft != []:
#                 answerLeft.pop()
#         else:
#             answerLeft.append(i)
#             cursor += 1
#     print(''.join(answerLeft)+''.join(answerRight[::-1]))

#고층건물 골드4 1027번
# n = int(input())
# total = list(map(int,input().split()))
# answer = []
# for i,v in enumerate(total):
#     count = 0
#     for i2,v2 in enumerate(total):
#         per = 0
#         if i > i2:
#             gap = v2 - v
#             for k in range(1,i-i2+1):
#                 if v + gap * (k/(i-i2)) <= total[i-k]:
#                     per += 1
#             if per == 1:
#                 count += 1
#         elif i < i2:
#             gap = v2 - v
#             for k in range(1, i2-i+1):
#                 if v + gap * (k / (i2 - i)) <= total[i+k]:
#                     per += 1
#             if per == 1:
#                 count += 1
#     answer.append(count)
#
# print(max(answer))

# 타겟넘버 프로그래머스 LV2
# def solution(numbers, target):
#     answer = []
#
#     def dfs(value,index):
#         if index != len(numbers):
#             dfs(value+numbers[index],index+1)
#             dfs(value-numbers[index],index+1)
#         else:
#             answer.append(value)
#
#     dfs(0,0)
#
#     return answer.count(target)

# 같은 숫자는 싫어 LV1
# def solution(arr):
#     answer = [arr[0]]
#     if len(arr) == 0:
#         return []
#     for i in arr[1:]:
#         if answer[-1] != i:
#             answer.append(i)
#     return answer

# 폰켓몬 LV1
# def solution(nums):
#     numsSet = list(set(nums))
#     if len(numsSet) < len(nums) / 2:
#         return len(numsSet)
#     return int(len(nums) / 2)
#
# print(solution([3,1,2,3]))
# print(solution([3,3,3,2,2,4]))
# print(solution([3,3,3,2,2,2]))

# 가운데 글자 가져오기 LV1
# def solution(s):
#     if len(s) % 2 == 0:
#         return s[len(s)//2 - 1:len(s)//2 + 1]
#     else:
#         return s[len(s)//2]

# def solution(numbers):
#     answer = set([])
#     for i in range(len(numbers)):
#         for value in (numbers[:i] + numbers[i+1:]):
#             answer.add(numbers[i]+value)
#     return sorted(list(answer))
#
# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))

# 부족한 금액 계산하기 LV2
# def solution(price, money, count):
#     total = 0
#     for i in range(1,count+1):
#         total += i*price
#     if total > money:
#         return total-money
#     else:
#         return 0

# 나누어 떨어지는 숫자 배 LV1
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i / divisor == i // divisor:
#             answer.append(i)
#     if len(answer) == 0:
#         return [-1]
#     return sorted(answer)

# 직사각형 별찍기
# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     print('*' * a)
