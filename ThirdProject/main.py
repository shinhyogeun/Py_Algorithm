#넓이 우선탐색
from collections import deque
#내 코드

'''graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [6, 8],
        [1, 7],
        ]

vi = [False] * 9

def bfs(startpoint):
    print(startpoint, end= " ")
    queue = deque()
    vi[0] = True
    vi[startpoint] = True
    queue.append(startpoint)
    a = True
    while a:
        for k in list(queue):
            for i in graph[k]:
                if vi[i] != True:
                    vi[i] = True
                    queue.append(i)
                    print(i,end= " ")
            queue.popleft()
        if False not in vi:
            a = False
bfs(1)'''

#카톡 페스티벌 1번 월드컵 문제

'''a,b,c,d = list(map(str,input().split()))
king = [[] for _ in range(6)]
king[0] = list(map(str,input().split()))
king[1] = list(map(str,input().split()))
king[2] = list(map(str,input().split()))
king[3] = list(map(str,input().split()))
king[4] = list(map(str,input().split()))
king[5]= list(map(str,input().split()))

#a의 승점 총점을 구하자
scoreOfa = 0
scoreOfb = 0
scoreOfc = 0
scoreOfd = 0

for i in king:
    if i[0] == a:
        scoreOfa += float(i[2]) * 3
        scoreOfa += float(i[3]) * 1
    elif i[0] == b:
        scoreOfb += float(i[2]) * 3
        scoreOfb += float(i[3]) * 1
    elif i[0] == c:
        scoreOfc += float(i[2]) * 3
        scoreOfc += float(i[3]) * 1
    elif i[0] == d:
        scoreOfd += float(i[2]) * 3
        scoreOfd += float(i[3]) * 1

    if i[1] == a:
        scoreOfa += float(i[4]) * 3
        scoreOfa += float(i[3]) * 1
    elif i[1] == b:
        scoreOfb += float(i[4]) * 3
        scoreOfb += float(i[3]) * 1
    elif i[1] == c:
        scoreOfc += float(i[4]) * 3
        scoreOfc += float(i[3]) * 1
    elif i[1] == d:
        scoreOfd += float(i[4]) * 3
        scoreOfd += float(i[3]) * 1

total = [scoreOfa,scoreOfb,scoreOfc,scoreOfd]
print(sorted(total, reverse= True))
# 몇명이 나랑 같지?
def same(a):
    howmanysame = -1
    for i in total:
        if a == i:
            howmanysame += 1
    return howmanysame

# 몇등이지?
def mixanMatch(sd):
        for j in sorted(total, reverse= True):
            if sd == j:
                return sorted(total, reverse= True).index(j)

def lastfunction(okok):
    if okok == [0,0]: print(float(1))
    if okok == [0,1]: print(float(1))
    if okok == [0,2]: print(float(2/3))
    if okok == [0,3]: print(float(1/2))
    if okok == [1,0]: print(float(1))
    if okok == [1,1]: print(float(1/2))
    if okok == [1,2]: print(float(1/3))
    if okok == [2,0]: print(float(0))
    if okok == [2,1]: print(float(0))
    if okok == [3,0]: print(float(0))

lastfunction([mixanMatch(scoreOfa),same(scoreOfa)])
lastfunction([mixanMatch(scoreOfb),same(scoreOfb)])
lastfunction([mixanMatch(scoreOfc),same(scoreOfc)])
lastfunction([mixanMatch(scoreOfd),same(scoreOfd)])'''

#음료수 얼려 먹기

'''l,m = map(int,input().split())
squre = [[0]*m for _ in range(l)]
for i in range(l):
    squre[i] = list(map(int,input().split()))

result = 0

def goAround(x,y):
    squre[x][y] = 9
    global result
    global i
    a = [-1,0,1,0]
    b = [0,1,0,-1]
    for i in range(4):
        if l-1>=x+a[i]>=0 and m-1>=y+b[i]>=0:
            if squre[x+a[i]][y+b[i]] == 0:
                # 갈 수 있는 뱡향이 있다면!!
                goAround(x+a[i],y+b[i])

for i in range(l):
    for n in range(m):
        if squre[i][n] == 0:
            result += 1
            goAround(i,n)

print(result)
for k in range(l):
    print(squre[k])'''

#미로 탈출 문제

#내 코드

'''l,m = map(int,input().split())
miro = [[0]*m for _ in range(l)]
for i in range(l):
    miro[i] = list(map(int,list(input())))
a = [0,1,0,-1]
b = [1,0,-1,0]
trigger = True
whereNow = [0,0]
result = 1
i = 0
while trigger:
    if l-1 >= whereNow[0]+a[i] >= 0 and m-1 >= whereNow[1]+b[i] >= 0:
        print(whereNow)
        if miro[whereNow[0]+a[i]][whereNow[1]+b[i]] == 0:
            i = i + 1 if i < 3 else 0
        else:
            whereNow = [whereNow[0]+a[i],whereNow[1]+b[i]]
            result += 1
            i = 0
        if whereNow == [l-1,m-1]:
            print(result)
            trigger = False
    else:
        i = i + 1 if i < 3 else 0'''

#갓동빈 코드
'''from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))

for i in range(n):
    print(graph[i])'''

#소수 구하기

'''a,b = map(int,input().split())
map = [1]*1000000
# index는 0 부터 999999까지
map[0] = 0
for i in range(0,1000000):
    if i == 0:
        continue
    if map[i] != 0:
        j = i+1
        while True:
            j = j + (i+1)
            if  j >= 1000000:
                break
            map[j-1] = 0
realmap = map[a-1:b]
s = 0
for i in range(len(realmap)):
    if realmap[i] == 1:
            print(a+i)'''


#선택정렬 알고리즘

'''a = [7,5,9,0,3,1,6,2,4,8]
for j in range(0,len(a)):
    min = a[j]
    for i in range(j,len(a)):
        if min > a[i]:
            min = a[i]
            index = i
    a[j], a[index] = a[index], a[j]
print(sorted(a))'''

#삽입정렬 알고리즘

#내 코드

'''a = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(a)):
    b = 0
    for j in range(i-1,-1,-1):
        if a[i] > a[j]:
            toss = a[i]
            a.remove(toss)
            a.insert(j+1,toss)
            break
        else :
            b += 1
    if b == i:
        toss = a[i]
        a.remove(toss)
        a.insert(0,toss)
    print(a)'''

# 갓동빈님 코드

'''array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
print(array)'''

# 퀵 정렬 알고리즘(어려움 주의)

#갓동빈 코드
'''def quickSort(arr,fro,to):
    pibut = fro
    left = fro+1
    right = to
    if len(arr) <= 1:
        return
    while left <= right:
        while left <= len(arr)-1 and arr[left] < arr[pibut]: left += 1
        while right >= 1 and arr[right] > arr[pibut] : right -= 1
        if left > right:
            arr[right], arr[pibut] = arr[pibut], arr[right]
            quickSort(arr,0,right-1)
            quickSort(arr,right+1,to)
        else:
            arr[left], arr[right] = arr[right], arr[left]

quickSort(array,0,9); print(array)'''


# 내 코드
'''array = [5,7,9,0,3,1,6,2,4,8]

def quick(array,start,end):
    pivot = start
    left = start+1
    right = end
    if len(array) <= 1:
        return
    while left <= right:
        for i in range(start+1,end):
            if array[i] > array[pivot]:
                left = i
                break
            else:
                left += 1
        for i in range(end,start,-1):
            if array[i] < array[pivot]:
                right = i
                break
            else:
                right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]
            quick(array,start,right-1)
            quick(array,right+1,end)

quick(array,0,9)
print(array)'''

#계수 정렬

'''array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
arr = [0]*(max(array)+1)
for i in array: arr[i] += 1
for i in range(len(arr)):
    for j in range(arr[i]):
        print(i, end= " ")'''

# 위에서 아래로

'''length = int(input())
checker = 0
arr = []
while checker < length:
    arr.append(int(input()))
    checker += 1
sortedarr = sorted(arr, reverse= True)

for i in sortedarr:
    print(i, end=" ")'''

# 성적이 낮으면 공부를 해야지

# 내 코드
'''length = int(input())
arr = []
scorearr = []

for i in range(length):
    ar = input().split()
    print(ar)
    arr.append(ar)
    scorearr.append(int(ar[1]))

scorearr.sort()

for i in scorearr:
    for j in arr:
        if int(j[1]) == i:
            print(j[0], end= " ")'''

# 갓동빈 코드

'''length = int(input())
arr = []
for i in range(length):
    inpp = input().split()
    arr.append((inpp[0],int(inpp[1])))
real = sorted(arr, key= lambda student:student[1])
for i in real:
    print(i[0], end=" ")'''
