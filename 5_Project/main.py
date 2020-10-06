# 1모험가 길드

'''n = int(input())
arr = list(map(int,input().split()))
arr.sort()

original = len(arr)
count = 0; ss = 0

while arr[0]+ss < len(arr):
    #만족한다.
    if max(arr[0:arr[0]+ss]) <= arr[0]+ss:
        count += 1
        print(arr[0:arr[ss]])
        del arr[0:arr[ss]]
        ss = 0
    # 만족안한다.
    else:
        ss += 1'''

'''print(count)'''

# 2곱하기 혹은 더하기

'''arr = list(map(int,input()))
result = arr[0]
for i in arr:
    if result == 0:
        result = result + i
    else:
        if i != 0 and i != 1:
            result = result * i
        else:
            result = result + i

print(result)'''

'''x = 0
y = 1-x
re = 0
for i in range(1,10):
    x += 0.1
    y = 1-x
    re += 0.1*x**3*y**2

print(re)

print("세타가 0.1이면 ",((1/9)*(0.1)**3*(0.9)**2)/0.0167)
print("세타가 0.2이면 ",((1/9)*(0.2)**3*(0.8)**2)/0.0167)
print("세타가 0.3이면 ",((1/9)*(0.3)**3*(0.7)**2)/0.0167)
print("세타가 0.4이면 ",((1/9)*(0.4)**3*(0.6)**2)/0.0167)
print("세타가 0.5이면 ",((1/9)*(0.5)**5)/0.0167)
print("세타가 0.6이면 ",((1/9)*(0.6)**3*(0.4)**2)/0.0167)
print("세타가 0.7이면 ",((1/9)*(0.7)**3*(0.3)**2)/0.0167)
print("세타가 0.8이면 ",((1/9)*(0.8)**3*(0.2)**2)/0.0167)
print("세타가 0.9이면 ",((1/9)*(0.9)**3*(0.1)**2)/0.0167)'''

# 3문자열 뒤집기
#이것은 비효율일까 아니면 다른 것일까?
'''arr = list(map(int,input()))
zero_zone = 0
zero = 0
one_zone = 0
one = 0
for i in range(len(arr)):
    if arr[i] == 0:
        if one != 0:
            one_zone += 1
            one = 0
        zero += 1
    elif arr[i] == 1:
        if zero != 0:
            zero_zone += 1
            zero = 0
        one += 1
    if i == len(arr)-1 :
        if arr[i] == 0:
            zero_zone += 1
        else:
            one_zone += 1

print(zero_zone,one_zone)'''

# 다른풀이
'''arr = list(map(int,input()))
zero_zone = 0
one_zone = 0
for i in range(len(arr)):
    if i == 0:
        if arr[0] == 0:
            zero_zone += 1
            continue
        elif arr[i] == 1 :
            one_zone += 1
            continue
    if arr[i] != arr[i-1]:
        if arr[i] == 1:
            one_zone += 1
        elif arr[i] == 0:
            zero_zone += 1
print(min(zero_zone,one_zone))'''

# 4.만들 수 없는 금액
'''answer = 1
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
a = 1

def find_remove(a,arr):
    arr2 = arr[:]
    if a < 0 or arr2 == []:
        return False
    if a == 0:
        return True
    for i in range(len(arr2)):
        if arr2[i] > a:
            a -= arr2[i-1]
            del arr2[i-1]
            return find_remove(a,arr2)
        if i == len(arr2)-1:
            a -= arr2[-1]
            del arr2[-1]
            return find_remove(a,arr2)

for i in range(1,sum(arr)+1):
    if find_remove(i,arr) == False:
        print(i)
        break'''

# 5.볼링공 고르기

'''n,m = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] != arr[j]:
          answer += 1
print(answer)'''

# 무지의 먹방 라이브~(정확도 100 효율성 쓰레기)

'''def count(a):
    ans = 0
    for i in range(len(a)):
        if a[i] != 0: ans += 1
    return ans

def mini(a):
    aa = []
    for i in a:
        if i != 0: aa.append(i)
    return min(aa)

def solution(food_times, k):
    answer = 0
    getin = True
    length = count(food_times)
    while k >= length or getin:
        getin = False
        a = mini(food_times)
        if k >= a*length :
            k -= a*length
            food_times = [food_times[i] - a if food_times[i]-a > 0 else 0 for i in range(len(food_times))]
            if food_times == [0]*len(food_times): return -1
        else:
            k = k%count(food_times)
            break
        length = count(food_times)

    for i in range(len(food_times)):
        if food_times[i] != 0: k -= 1
        if k == -1:
            answer = i+1
            break
    return answer'''

# 갓동빈 코드

'''import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value+(q[0][0]-previous)*length <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1
        previous = now

    result = sorted(q,key=lambda x:x[1])
    return result[(k-sum_value)%length][1]'''

#럭키 스트라이크
'''arr = list(map(int,input()))
a = 0
b = 0
for i in range(1,len(arr)+1):
    if i <= len(arr)/2:
        a += arr[i-1]
    else:
        b += arr[i-1]
if a == b: print("LUCKY")
else:
    print("READY")'''

#문자열 재정렬

'''arr = list(map(str,input()))
a = []
b = []
for i in range(len(arr)):
    if ord(arr[i]) >= 65:
        a.append(arr[i])
    else:
        b.append(int(arr[i]))

a.sort()
print("".join(a) + str(sum(b)))'''

# 자물쇠와 열쇠

# 회전!

'''def right(total_l, key_l, lock_l, mother_matrix, ans):
    for i in range(total_l):
        for j in range(total_l):
            if key_l - 1 <= i <= key_l + lock_l - 2 and key_l - 1 <= j <= key_l + lock_l - 2:
                if mother_matrix[i][j] == 1: ans += 1
                else: return False
    if ans == lock_l ** 2: return True

def tilt_it(x):
    real = [[0]*len(x) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            real[j][-(i+1)] = x[i][j]
    return real

def solution(key, lock):
    lock_l = len(lock)
    key_l = len(key)
    total_l = lock_l+(key_l*2-2)
    a = 0 ; b = 0; c = 0

    # 거대한 행렬에 기본 셋팅
    mother_matrix = [[0] * total_l for i in range(total_l)]
    for i in range(total_l):
        for j in range(total_l):
            if key_l - 1 <= i <= key_l + lock_l - 2 and key_l - 1 <= j <= key_l + lock_l - 2:
                mother_matrix[i][j] = lock[i - (key_l - 1)][j - (key_l - 1)]
    # 거대한 행렬에 기본 셋팅2
    for i in range(key_l):
        for j in range(key_l):
            mother_matrix[i][j] += key[i][j]

    while True:

        # 확인작업맞으면!
        if right(total_l,key_l,lock_l,mother_matrix,0):
            return True
        else:

        # 확인작업틀리면 지우기 작업!
            for i in range(a,key_l+a):
                for j in range(b,key_l+b):
                    mother_matrix[i][j] -= key[i-a][j-b]
            b += 1
            if key_l+b > total_l: a += 1;b = 0
            if key_l+a > total_l :
            #이동작업도 안되면 회전작업
                key = tilt_it(key)
                c += 1
                # 거대한 행렬에 기본 셋팅
                mother_matrix = [[0] * total_l for i in range(total_l)]
                for i in range(total_l):
                    for j in range(total_l):
                        if key_l-1 <= i <= key_l + lock_l-2 and key_l-1 <= j <= key_l+lock_l-2:
                            mother_matrix[i][j] = lock[i-(key_l-1)][j-(key_l-1)]
                a = 0
                b = 0
            # 회전을 다했음에도 안되면 안열리는것이다.
                if c == 4: return False
            # 확인작업틀리면 새로그리기 작업!
            for i in range(a, key_l+a):
                for j in range(b, key_l+b):
                    mother_matrix[i][j] += key[i-a][j-b]

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))'''

#뱀
'''n = int(input())
miro = [[0]*(n+1) for i in range(n+1)]
turning_point = []
for i in range(int(input())):
    s,t = list(map(int,input().split()))
    miro[s][t] = 9
for i in range(int(input())):
    turning_point.append(list(map(str,input().split())))
c = 1; d = 1; ss=0
sharft = [[0,1],[1,0],[0,-1],[-1,0]]

miro[c][d] = 1
sharft_now = 0
answer = 0
snake = [[1,1]]
def check_snake(a,b):
    for i in a:
        miro[i[0]][i[1]] = 1
    if b == True:
        miro[a[0][0]][a[0][1]] = 0

while True:
    answer += 1
    c += sharft[sharft_now][0]; d += sharft[sharft_now][1]
    #outofBounds이면 멈춰라
    if c > n or c < 1 or d > n or d < 1:
        print(answer)
        break
    #사과가 있으면 꼬리 안 자르고 이동!
    if miro[c][d] == 9:
        snake.append([c,d])
        check_snake(snake,False)
    #자기몸이면!!
    elif miro[c][d] == 1:
        print(answer)
        break
    #사과도 없고 그냥 평범한 이동!
    else:
        snake.append([c,d])
        check_snake(snake,True)
        del snake[0]
    # 회전해야하면 해라!
    if answer == int(turning_point[ss][0]):
        print(ss)
        if turning_point[ss][1] == "D":
            sharft_now = sharft_now + 1 if sharft_now < 3 else 0
        else:
            sharft_now = sharft_now - 1 if sharft_now > 0 else 3
        ss = ss + 1 if ss < len(turning_point) - 1 else 0'''

#기둥과 보(기둥은 0로 보는 1로 표시합니다.)

#설치가 가능한가요?
'''def ok(ans):
    for i in ans:
        x,y,stuff = i
        # 기둥일 경우
        if stuff == 0:
            if y == 0 or [x,y-1,0] in ans or [x-1,y,1] in ans or [x,y,1] in ans:
                continue
            else: return False
        #보일 경우
        else:
            if [x,y-1,0] in ans or [x+1,y-1,0] in ans or ([x-1,y,1] in ans and [x+1,y,1] in ans):
                continue
            else: return False
    return True
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        if i[3] == 1:
            answer.append([i[0],i[1],i[2]])
            if ok(answer) == False:
                answer.remove([i[0],i[1],i[2]])
        elif i[3] == 0:
            answer.remove([i[0],i[1],i[2]])
            if ok(answer) == False:
                answer.append([i[0],i[1],i[2]])
    answer.sort()
    return answer

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))'''

# 연산자 끼워넣기
'''n = int(input())
arr = list(map(int,input().split()))
ss = list(map(int,input().split()))
final = []

def calimax(arr,k,ss,final_component):
    if k == len(arr)-1:
        final.append(final_component)
    else:
        for i in range(4):
            if ss[i] != 0:
                repla = ss[:]
                repla[i] = repla[i] - 1
                if i == 0:
                    calimax(arr, k+1, repla, final_component+arr[k+1])
                if i == 1:
                    calimax(arr, k + 1, repla, final_component-arr[k+1])
                if i == 2:
                    calimax(arr, k + 1, repla, final_component*arr[k+1])
                if i == 3:
                    calimax(arr, k + 1, repla, int(final_component/arr[k + 1]))

calimax(arr,0,ss,arr[0])
print(max(final))
print(min(final))'''

# 치킨배달
'''from itertools import combinations
n,m = map(int,input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
real = []
for i in range(1,n+1):
    a = list(map(int, input().split()))
    for j in range(n):
        arr[i][j+1] = a[j]
house = []
chick = []

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chick.append((i,j))

def ck_distance(ho,ch):
    ans = 0
    for i in ho:
        re = []
        for j in ch:
            re.append(abs(i[0]-j[0]) + abs(i[1]-j[1]))
        ans += min(re)
    return ans

for i in list(combinations(chick,m)):
    real.append(ck_distance(house,i))
print(min(real))'''

# 특정거리의 도시 찾기
'''from collections import deque

n,m,k,x = map(int,input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)

visited = [False]*(n+1)
dis = [0]*(n+1)
queue = deque([x])
visited[x] = True

while queue:
    v = queue.popleft()
    for i in arr[v]:
        if not visited[i]:
            dis[i] = dis[v] + 1
            visited[i] = True
            queue.append(i)

for i in range(1,len(dis)):
    if dis[i] == k:
      print(i)

if k not in dis:
    print(-1)'''

#10000보다 작은 소수를 모두 찾으시오.(에라토테네스의 체)
'''a = [i for i in range(1,10001)]
b = [True]*10001
for i in range(1,10001):
    if b[i] == True:
        for j in range(2,10000):
            if a[i] * j > 10000: break
            else: b[a[i]*j] = False
for i in range(1,len(b)):
    if b[i] == True:
        print(i)'''

#연구소

'''from itertools import combinations

l,m = map(int,input().split())
arr2 = [[0] * m for i in range(l)]
a = 1
arr = []
emp = []
vir = []
last = []
result = 0
for i in range(l):
    arr.append(list(map(int,input().split())))
# 바이러스를 퍼지게하는 함수이다.
def DFS(arr3,start):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for j in range(4):
        if l>start[0]+dx[j]>=0 and m>start[1]+dy[j]>=0 :
            if arr3[start[0]+dx[j]][start[1]+dy[j]] == 0:
                arr3[start[0]+dx[j]][start[1]+dy[j]] = 2
                DFS(arr3,[start[0]+dx[j],start[1]+dy[j]])

for i in range(l):
    for j in range(m):
        if arr[i][j] == 0:
            emp.append([i,j])
        if arr[i][j] == 2:
            vir.append([i,j])
real = 0
for i in combinations(emp,3):
    for k in range(l):
        for j in range(m):
            arr2[k][j] = arr[k][j]
    count = 0
    arr2[i[0][0]][i[0][1]] = 1
    arr2[i[1][0]][i[1][1]] = 1
    arr2[i[2][0]][i[2][1]] = 1
    for j in vir:
        DFS(arr2,j)
    for k in range(l):
        for j in range(m):
            if arr2[k][j] == 0:
                count += 1
    real = max(real,count)

print(real)'''

# 1로 만들기
'''arr = []
kk = [0]*30001
# 최소 연산갯수를 반환해주는 함수이다.
def make_1(a):
    # 5로 나누어 떨어지면!
    if a != int(a):
        return 40000
    if kk[int(a)] != 0:
        return kk[int(a)]
    if a in [2,3,5]:
        kk[int(a)] = 1
        return 1
    kk[int(a)] = min(make_1(a-1),make_1(a/5),make_1(a/3),make_1(a/2)) + 1
    return kk[int(a)]
print(make_1(1000))'''

#경쟁적 전염
'''from collections import deque

queue = deque()
n,k = map(int,input().split())
arr = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    arr.append(list(map(int,input().split())))
s,X,Y = map(int,input().split())

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            queue.append([arr[i][j],i,j])

for i in range(s):
    length = len(queue)
    while length >= 1:
        what,x,y = queue.popleft()
        for i in range(4):
            if k > x + dx[i] >=0 and k > y + dy[i] >=0:
                if arr[x+dx[i]][y+dy[i]] == 0 :
                    arr[x+dx[i]][y+dy[i]] = what
                elif arr[x+dx[i]][y+dy[i]] > what:
                    arr[x+dx[i]][y+dy[i]] = what
        length -= 1

if arr[X-1][Y-1] != 0:
    print(arr[X-1][Y-1])
else:
    print(0)'''

#국영수
'''n = int(input())
arr = []

for i in range(n):
    name,guk,eng,mat = input().split()
    arr.append((int(guk),int(eng),int(mat),name))

fin = sorted(arr,key=lambda x : (-x[0],x[1],-x[2],x[3]))

for i in fin:
    print(i[3])'''

#안테나
'''n = int(input())
house = list(map(int,input()))
arr = []
min = 1e9
where = 0
for i in range(len(house)):
    toss = 0
    for j in range(len(house)):
        toss += abs(house[i] - house[j])
    if toss < min:
        min = toss
        where = i
print(house[where])'''

#실패율(카카오 코테)
'''def solution(N, stages):
    #각 단계별로 실패율을 구하자.
    king = []
    answer = []
    for i in range(1,N+1):
        sun = 0
        mom = 0
        for k in stages:
            if k >= i :
                mom += 1
                if k == i:
                    sun += 1
        if mom == 0 :
            failurate = 0
        else:
            failurate = sun/mom
        king.append((failurate,i))
    fin = sorted(king,key=lambda x : (-x[0],x[1]))
    for i in fin:
        answer.append(i[1])
    return answer
solution(5,[2, 1, 2, 6, 2, 4, 3, 3])'''

#카드정렬하기

'''n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
length = len(arr)
ans = 0
for i in range(length):
        if i in [0,1]:
            ans += arr[i]*(length-1)
        else:
            ans += arr[i]*(length-i)
print(ans)'''

# 정렬된 배열에서 특정 수의 개수 구하기
'''from bisect import bisect_left, bisect_right

a,b = map(int,input().split())
arr = list(map(int,input().split()))
def count(total,le,ri):
    right_index = bisect_right(arr,ri)
    left_index = bisect_left(arr,le)
    return right_index - left_index

if count(arr,b,b) == 0:
    print(-1)
else:
    print(count(arr,b,b))'''


# 정렬된 배열에서 특정 수의 개수 구하기 (이진탐색 직접구현)

'''def findout(arr,dd,frm,to):
    pivot = (to+frm)//2
    if frm > to:
        return None
    print(frm,to)
    if arr[pivot] > dd :
        return findout(arr,dd,frm,pivot-1)
    elif arr[pivot] < dd:
        return findout(arr,dd,pivot+1,to)
    else :
        return pivot
print(findout([1,2,3,4,6,7,8,9],5,0,7))'''


#고정점 찾기
'''n = int(input())
arr = list(map(int,input().split()))
asw = []

def find_out(arr,frm,to):
    if frm > to :
        return None
    pivot = (frm + to) // 2
    if arr[pivot] > pivot :
        return find_out(arr,frm,pivot-1)
    elif arr[pivot] < pivot :
        return find_out(arr,pivot+1,to)
    else:
        asw.append(pivot)
        return find_out(arr,frm,pivot-1), find_out(arr, pivot + 1, to)

find_out(arr,0,len(arr)-1)

if asw == []:
    print(-1)
else:
    for i in asw:
        print(i)'''

#공유기 설치











