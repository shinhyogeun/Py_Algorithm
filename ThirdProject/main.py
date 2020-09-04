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

# 두 배열의 원소 교체
'''n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [sorted(b,reverse=True)[i] - sorted(a)[i] for i in range(len(a))]
result = sum(a)
for i in range(k):
    if c[i] > 0:
        result += c[i]
print(result)'''

#이진 탐색(꼭 암기하자)

# 이 함수는 배열과 원하는 원소를 넣으면 그 원소가 있는 index를 반환하는 함수입니다.
'''def binary_searching(arr,start,end,want):
    #기준은 index입니다.
    print("여기1")
    middle = int(end-start/2)
    if arr[middle] > want:
        print("여기2")
        end = middle-1
        start = 0
        binary_searching(arr,start,end,want)
    elif arr[middle] < want:
        print("여기3")
        end = len(arr)-1
        start = middle+1
        binary_searching(arr, start, end, want)
    else:
        print(middle)
        return middle

array = [0,2,4,6,8,10,12,14,16,18]
print(binary_searching(array,0,9,7))'''

# 부품 찾기

'''n = int(input())
parent = list(map(int,input().split()))
m = int(input())
wanted = list(map(int,input().split()))

def is_that_right(arr,start,end,want):
    if end<=start:
        if arr[end] == want:
            print("yes",end=" ")
            return
        else:
            print("no",end=" ")
            return
    middle = start + int((end-start)/2)
    if arr[middle] < want:
        is_that_right(arr,middle+1,end,want)
    elif arr[middle] == want:
        print("yes",end=" ")
        return
    else:
        is_that_right(arr,start,middle-1,want)

for i in range(len(wanted)):
    sun = wanted[i]
    is_that_right(parent,0,len(parent)-1,sun)'''

# 떡볶이 떡 만들기

#내코드
'''n,m = map(int,input().split())
total = list(map(int,input().split()))

sorted_total = sorted(total,reverse=True)

max_value_in_total = sorted_total[0]

array_that_we_have_to_get_answer_from = []
sums = 0
for i in range(max_value_in_total,-1,-1):
    for j in range(len(sorted_total)-1):
        if sorted_total[j]-i <= 0:
            break
        else:
            sums += sorted_total[j]-i
    array_that_we_have_to_get_answer_from.append(sums)
    sums = 0

def findout(arr,start,end,want):
    middle = start + int((end-start)/2)
    middle_value = arr[middle]
    if end <= start:
        if middle_value >= m:
            return print(max_value_in_total - (middle))
        elif middle_value < m :
            return print(max_value_in_total - (middle+1))

    if middle_value < want:
        findout(arr,middle+1,end,want)
    elif middle_value > want:
        findout(arr,start,middle-1,want)
    else:
        return print(max_value_in_total - middle)

findout(array_that_we_have_to_get_answer_from,0,len(array_that_we_have_to_get_answer_from)-1,m)'''

# 갓동빈 코드
'''n,m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

while start <= end:
    total = 0
    middle = start + int((end-start)/2)

    for i in array:
        if i > array[middle]:
           total += i - array[middle]

    if total > m:
        end = middle - 1
    elif total <= m:
        result = total
        start = middle + 1'''


# 멱급수 만들기(업다운)
'''arr = [0]*10001
def pibo(s):
    if s == 1 or 2: return 1
    if arr[s] != 0 : return arr[s]
    else:
        arr[s] = pibo(s-1) + pibo(s-2)
        return arr[s]
print(pibo(100))'''

# 멱급수 만들기(다운업)
'''이 방식이 많이 쓰인다!'''

'''arr = [0]*1000
arr[1] = 1; arr[2] = 1
for i in range(3,len(arr)):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[99])'''

# 1로 만들기

#업다운
'''ab = int(input())

parent = [0] * 30001

def find(real):
    if real != int(real):
        return 121545
    if real == 1 or real == 2 or real == 3 or real == 5:
        return 1
    elif real == 4:
        return 2
    else:
        if parent[int(real)] != 0:
            return parent[int(real)]
        else:
            parent[int(real)] = min([find(real/5),find(real/3),find(real/2),find(real-1)]) + 1
            return parent[int(real)]
print(find(ab))'''

#다운업

'''parent = [0]*11
ab = int(input())
parent[1] = 0; parent[2] = 1; parent[3] = 1; parent[4] = 2; parent[5] = 1

for i in range(6,len(parent)):
    parent[i] = parent[i-1] + 1
    #5로 나눠진다.
    if parent[i] % 5 == 0:
        parent[i] = min(parent[i//5]+1,parent[i])
    if parent[i] % 3 == 0 :
        parent[i] = min(parent[i//3]+1,parent[i])
    if parent[i] % 2 == 0 :
        parent[i] = min(parent[i//2]+1,parent[i])'''


#개미전사

'''n = int(input())
arr = list(map(int,input().split()))
ans = [0]*(len(arr)+1)
trash = []
for i in range(2,len(arr)):

    if i == 2:
        ans[i+1] = arr[0] + arr[2]
    else:
        for j in range(i-1):
            trash.append(arr[i]+arr[j])
        compare = max(trash)
        trash = []
        ans[i+1] = max(ans[i],compare)

print(ans[n])

d = [0]*100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])

print(d[n-1])'''

# 민상이가 풀어보라는 문제

'''arr = list(input())
scorearr = []
for i in range(len(arr)):
    returnValue = 0
    if arr[i] != "(" and arr[i] != "{" and arr[i] != "[" and arr[i] != "]" and arr[i] != "}" and arr[i] != ")"  :
        for j in range(i,-1,-1):
            if arr[j] == ']'or arr[j] == ')' or arr[j] == '}':
                break
            if arr[j] == '(':
                returnValue += 1
            elif arr[j] == '{':
                returnValue += 2
            elif arr[j] == '[':
                returnValue += 3
        scorearr.append(returnValue)
        returnValue = 0
print(max(scorearr))'''

# PPAP

'''arr = list(input())
i = 0
while i < len(arr)-3:
    if arr[i] == "P":
        if [arr[i+1],arr[i+2],arr[i+3]] == ["P","A","P"]:
            del arr[i+1]
            del arr[i+1]
            del arr[i+1]
            i -= 1
            print(i)
        else :
            i += 1
    else:
        i += 1

if arr == ["P"]:
    print("PPAP")
else:
    print("NP")'''


'''arr2 = list(input())

def ppap(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] == "P":
            count += 1
        elif arr[i] == "A" and i+1 <= len(arr)-1:
            if count >= 2 and arr[i+1] == "P":
                count -= 1
                i += 1
            else:
                return print("NP")
        else:
            return print("NP")
        i += 1
    if count == 1 :
        return print("PPAP")
    else :
        return print("NP")

ppap(arr2)'''

# 바닥 공사
#      1 2 3 일 때
'''arr = [0]*1001
arr[1] = 1 ; arr[2] = 3 ; arr[3] = 5
n = int(input())

def find(a):
    if arr[a] != 0 :
        return arr[a]
    else:
        arr[a] = find(a-1) + 2 * (find(a-2))
        return arr[a]
print(find(n))'''

#효율적인 화폐구성