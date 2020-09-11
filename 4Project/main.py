# 다익스트라 구현

'''n,m = map(int,input().split())
start = int(input())
line = [[] for _ in range(n+1)]
visited = [False]*(n+1)
visited[0] = True
distance = [101]*(n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    line[a].append((b,c))


def smallted_among_remain():
    value = 101
    wher = 0
    for i in range(1,n+1):
        if distance[i] < value and not visited[i] :
            wher = i
    return wher

def dijekstra(start):
    global distance
    distance[start] = 0
    while visited != [True] * (n+1):
        a = smallted_among_remain()
        visited[a] = True
        for i in line[a]:
            if distance[a] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[a] + i[1]

dijekstra(start)
for i in range(1,len(distance)):
    if distance[i] == 101:
        print("INFINITY")
    else:
        print(distance[i])'''

# 개선된 다익스트라 알고리즘(힙정렬을 활용)

'''import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        real = heapq.heappop(q)
        if real[0] > distance[real[1]]: continue
        for i in graph[real[1]]:
            if real[0] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[real[1]] + i[1]
                heapq.heappush(q,(real[0] + i[1],i[0]))

dijkstra(start)

for i in distance:
    if i == INF :
        print("INFINITY")
    else:
        print(i)'''

# 플로이드 워셜 알고리즘

'''INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1,n+1):
    for k in range(1,n+1):
        if i == k : graph[i][k] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for k in range(1,n+1):
        if graph[i][k] == INF :
            print("INFINITY")
        else:
            print(graph[i][k], end= " ")
    print()'''

# 미래도시
'''INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n):
    for k in range(n):
        if i == k : graph[i][k] = 0

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    for k in range(1,n+1):
        for j in range(1,n+1):
            graph[k][j] = min(graph[k][j],graph[k][i]+graph[i][j])

x,k = map(int,input().split())
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])'''



#전보

'''import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
distance[0] = 0
for i in range(m):
    a,b,dis = map(int,input().split())
    graph[a].append((dis,b))

def dijkstar(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dis2,wher = heapq.heappop(q)
        if distance[wher] < dis2 : continue
        for i in graph[wher]:
            if i[0] + dis2 < distance[i[1]]:
                distance[i[1]] = i[0] + dis2
                heapq.heappush(q,(distance[i[1]],i[1]))

dijkstar(c)
total = 0

for i in range(1,n+1):
    if distance[i] != INF and i != c:
        total += 1
    elif distance[i] == INF:
        distance[i] = -1

print(total, max(distance))'''

# 서로소 구하기

'''n,m = map(int,input().split())

# 재료 : 루트노드 저장소
root = [0]*(n+1)

# 시작전 자기 자신을 루트로!
for i in range(1,n+1):
    root[i] = i

# 루트를 찾는 것!
def find_root(a):
    if root[a] != a:
        root[a] = find_root(root[a])
    return root[a]

#합치기
def union(a,b):
    if find_root(a) < find_root(b):
        root[b] = find_root(a)
    else:
        root[a] = find_root(b)

for i in range(m):
    a,b = map(int,input().split())
    union(a,b)

# 출력하자
    print(root)'''

'''def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        for i in range(1,len(parent)):
            if parent[i] == b:
                parent[i] = a
    else:
        for i in range(1, len(parent)):
            if parent[i] == a:
                parent[i] = b

v, e = map(int,input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent,a,b)

print(parent)'''


# 특정 원소가 속한 집합을 찾기
'''def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')'''

#사이클 판별

'''n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i] = i

def find_root(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find_root(parent[a])
        return parent[a]

def union(parent,a,b):
    if find_root(a) == find_root(b):
        print("Cycle occured in this moments")
        return
    else:
        if find_root(a) > find_root(b):
            parent[a] = b
        else:
            parent[b] = a

for i in range(m):
    a,b = map(int,input().split())
    union(parent,a,b)'''

# 크루스칼 알고리즘(최소비용으로 신장트리를 만드는 알고리)

'''n,m = map(int,input().split())
e = []
root = [0]*(n+1)
result = 0

for i in range(n+1):
    root[i] = i

def find_parent(a):
    if root[a] == a:
        return a
    else:
        root[a] = find_parent(root[a])
        return root[a]

for i in range(m):
    a,b,c = map(int,input().split())
    e.append((c,a,b))

e.sort()

def union(root,a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b :
        root[a] = b
    else:
        root[b] = a

for i in range(len(e)):
    if find_parent(e[i][1]) == find_parent(e[i][2]):
        continue
    else:
        union(root,e[i][1],e[i][2])
        result += e[i][0]

print(result)'''

# 팀결성

'''n,m = map(int,input().split())

parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i] = i

def find_parent(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find_parent(parent[a])
        return parent[a]

def union(parent,a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a

def same_team(a,b):
    if find_parent(a) == find_parent(b):
        print("YES")
    else:
        print("NO")

for i in range(m):
    a,b,c = map(int,input().split())
    if a == 1:
        same_team(b,c)
    elif a == 0:
        union(parent,b,c)'''

# 도시 분할 계획

'''n,m = map(int,input().split())
parent = [0]*(n+1)
e = []
cost2 = 0
woo = []
for i in range(1,n+1):
    parent[i] = i

def find_parent(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find_parent(parent[a])
        return parent[a]

def union(parent,a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    a,b,cost = map(int,input().split())
    e.append((cost,a,b))

e.sort()

for i in range(len(e)):
    if find_parent(e[i][1]) == find_parent(e[i][2]):
        continue
    else:
        union(parent,e[i][1],e[i][2])
        woo.append(e[i][0])
        cost2 += e[i][0]
print(woo)
print(cost2)
print(max(woo))
print(cost2-max(woo))'''

#괄호변환(카카오 문제)

'''def right(p):
    a = 0
    b = 0
    for i in p:
        if i == "(":
            a += 1
        elif i == ")":
            b += 1
        if a - b < 0: return False
    if a - b == 0:
        return True
    else:
        return False


def formchange(list):
    result = ""
    print(list)
    for i in list:
        result = result + str(i)
    print("form문제",result)
    return result


def change(p):
    if len(p) < 3:
        return []
    else:
        print("들어가기전P",p)
        del p[0]
        del p[len(p) - 1]
        print("들어가기전2P", p)
        for i in range(len(p)):
            print(i)
            if p[i] == "(":
                p[i] = ")"
                continue
            if p[i] == ")":
                p[i] = "("
        print("p",p)
        return p


def split(list):
    u = ""
    v = ""
    a = 0
    b = 0
    for i in list:
        if i == "(":
            a += 1
        elif i == ")":
            b += 1
        if a == b: break

    u = list[0:a + b]
    u = "".join(u)
    v = list[a + b:]
    v = "".join(v)
    return u, v


def solution(p):
    if p == "": return ""
    listp = list(p)
    list_result = []

    if right(listp):
        return p
    else:
        # u,v로 분리
        u, v = split(listp)
        listu = list(u)
        listv = list(v)
        print(u)
        print(v)
        if right(listu):
            listu.append(solution(v))
            return formchange(listu)
        else:
            list_result.append("(")
            list_result = list_result + list(solution(v))
            list_result.append(")")
            list_result = list_result + change(listu)
            answer = formchange(list_result)
            return answer

for i in range(3):
    print("함수실행결과",solution(input()))'''

#외벽 점검(카카오 문제)

'''def solution(n, weak, dist):
    answer = 1
    length = len(weak)
    dist = sorted(dist)
    print(dist)
    for i in range(length):
        weak.append(weak[i] + n)

    answer2 = gime_me_answer(answer, weak, dist, length)
    return answer2

def gime_me_answer(answer, weak, dist, length):
    # 출발점 설정
    aaa = []
    for i in range(length):
        # 1명으로 커버가 가능합니다.
        if weak[i] + dist[-answer] >= weak[i + (length - 1)]:
            aaa.append(answer)
        # 한 친구가 더 필요합니다.
        else:
            realtoss = find_where(weak[i]+dist[-answer],weak)
            aaa.append(add_one(weak, dist, answer,i, length,realtoss))
    real = aaa
    real.sort()
    print(real)
    if real[0] == 10 :
        return -1
    else:
        return real[0]


# 이 함수는 "친구한명 추가하면 가능해요? 그럴경우 answer를 반납하고 다 추가해도 안되면 10을 반환해주세요."를 실행한다.
def add_one(weak, dist, answer, i, length, realtoss):
    answer += 1
    if answer > len(dist):
        return 10
    if i == 3:
        print(weak[realtoss] + dist[-answer])
        print(weak[i+(length-1)])
    if weak[realtoss] + dist[-answer] >= weak[i+(length-1)]:
        return answer
    else:
        realtoss = find_where(weak[realtoss] + dist[-answer], weak)
        return add_one(weak, dist, answer, i, length, realtoss)

def find_where(a, weak):
    for i in range(len(weak)):
        if weak[i] > a:
            return i

print(solution(200, [0, 10, 50, 80, 120, 160],[1, 10, 5, 40, 30]))'''

#문자열 압축(카카오)

'''def solution(s):
    apple = []
    if len(s) == 1:
        return 1
    else:
        for i in range(1,len(s)//2+1):
            apple.append(check_this_out(s,i))
        return min(apple)

def check_this_out(s,i):
    # s[i*(j-1):i*j] VS s[i*j:i*j+i]
    a = 1
    sdsd = ""
    for j in range(1,len(s)//i+2):
        if s[i*(j-1):i*j] != s[i*j:i*j+i]:
            if a == 1:
                real1 = "".join(s[i*(j-1):i*j])
            elif a > 1:
                real1 = str(a) + "".join(s[i*(j-1):i*j])
            sdsd += real1
            a = 1
        else:
            a += 1
            if a == len(s)//i+2:
                real1 = str(a) + "".join(s[i*(j-1):i * j])
                sdsd += real1
    return len(sdsd)

print(solution("a"))'''



def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    print(words[1:] + [''])
    for a, b in zip(words, words[1:] + ['']):
        print("a = ",a, "b = ", b)
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))