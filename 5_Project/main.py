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
'''n,c = map(int,input().split())
arr = []
maxim = 0

for i in range(n):
    arr.append(int(input()))

arr.sort()

min2 = arr[1]-arr[0]
max2 = arr[-1]-arr[0]
result = 0
def find_out(arr,min,max):
    global result
    point = arr[0]
    pivot = (min + max) // 2
    wifi_num = 1

    if min > max :
        return

    for i in range(1,n):
        if arr[i] - point >= pivot:
            wifi_num += 1

    # 너무 많은 공유기가 설치되었어 그래서 공유기를 줄이려고 피벗을 늘려야 해!
    if wifi_num > c :
        return find_out(arr,pivot+1,max)
    # 너무 적은 공유기가 설치되었어 그래서 더 많은 공유기를 설치하려고 피벗을 줄여야 해!
    elif wifi_num <= c :
        result = wifi_num
        return find_out(arr, min, pivot-1)
    # 딱 적당해!
find_out(arr,min2,max2)
print(result)'''

# 가사 검색(카카오 코테)
'''from bisect import bisect_left, bisect_right

def count_by_range(a,left,right):
    right_index = bisect_right(a,right)
    left_index = bisect_left(a,left)
    return right_index - left_index

arr_lenght = [[] for _ in range(10001)]
re_arr_lenght = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for i in words:
        arr_lenght[len(i)].append(i)
        re_arr_lenght[len(i)].append(i[::-1])

    for i in range(10001):
        arr_lenght[i].sort()
        re_arr_lenght[i].sort()

    for i in queries:
        start = ""
        end = ""
        reverse = False
        if i[0] == "?":
            i = i[::-1]
            reverse = True
        for h in i:
            if h != "?":
                start += h
                end += h
            else:
                start += "a"
                end += "z"
        if reverse == True:
            answer.append(count_by_range(re_arr_lenght[len(i)],start,end))
        else:
            answer.append(count_by_range(arr_lenght[len(i)], start, end))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))'''

# 금 광
'''m = int(input())
for i in range(m):
    l,n = map(int,input().split())
    arr = []
    real = []
    arre = list(map(int,input().split()))
    for i in range(l):
        arr.append(arre[n*i:n*(i+1)])
    for j in range(n):
        a = []
        for i in range(l):
            a.append(arr[i][j])
        real.append(a)
    for i in range(1,n):
        for j in range(l):
            if j == 0:
                real[i][j] += max(real[i-1][j],real[i-1][j+1])
            elif j == l-1:
                real[i][j] += max(real[i-1][j-1],real[i-1][j])
            else:
                real[i][j] += max(real[i-1][j-1],real[i-1][j],real[i-1][j+1])
    print(max(real[n-1]))'''

# a2의 1행에 = max (a2의 1행 +a1의 1행,a)
'''import math
ss = [True]*10001 
for i in range(2,10000):
    if ss[i] == True :
        for j in range(2,10000):
            if i*j <= 10000 :
                ss[i*j] = False
            else: break
ss[0] = False;ss[1] = False
for i in range(len(ss)):
    if ss[i] == True:
        print(i)'''

# 다익스트라 구현
'''import heapq

INF = 1e9
node,line = map(int,input().split())
start = int(input())
real = [[] for _ in range(node+1)]
answer = [INF]*(node+1)
answer[start] = 0
q = []
heapq.heappush(q,[0,start])

for i in range(line):
    a,b,c = map(int,input().split())
    real[a].append((b,c))

while q:
    dis,where = heapq.heappop(q)
    for i in real[where]:
        if answer[i[0]] > dis+i[1]:
            heapq.heappush(q,[dis+i[1],i[0]])
            answer[i[0]] = dis+i[1]

for i in range(1,answer):
    print(answer[i])'''

# 사이클 판별
'''node, line = map(int,input().split())
store = [0]*(node+1)
for i in range(1,node+1):
    store[i] = i

def find_parent(store,a):
    if store[a] != a:
        store[a] = find_parent(store,store[a])
    return store[a]

def is_cycle_occured():
    for i in range(line):
        a, b = map(int, input().split())
        root_a = find_parent(store,a)
        root_b = find_parent(store,b)
        if root_a > root_b:
            store[a] = root_b
        elif root_a < root_b:
            store[b] = root_a
        else:
            return "Yes it Occured"
    return "No that is not Occured"

print(is_cycle_occured())'''

#쿠팡 1번

'''def solution(N):
    answer = []
    for i in range(2,10):
        result = ""
        a = N
        while a // i >= 1:
            core = a % i
            a = a // i
            result = str(core) + result
            if a < i :
                result = str(a) + result
        k = list(map(int,result))
        value = 1
        for j in k:
            if j == 0:
                continue
            else:
                value = value * j
        answer.append([i,value])
    real = sorted(answer,key=lambda x : (x[1],x[0]), reverse=True)
    return real[0]'''

'''def solution(depar,hub,dest,roads):
    total = set()
    frm = 0
    to = 0
    toss = 0
    for i in roads:
        c = {i[0], i[1]}
        total = total | c
    arr = dict()
    for i in range(len(total)):
        ss = list(total)[i]
        arr[ss] = i+1
    for i in arr:
        if i == depar:
            frm = arr[i]
        elif i == hub:
            toss = arr[i]
        elif i == dest:
            to = arr[i]
    n = len(arr)
    graph = [[0]*(n+1) for i in range(n+1)]
    for i in roads:
        graph[arr[i[0]]][arr[i[1]]] = 1
    visited = [False] * (n+1)
    def DFS(frm,to,cnt):
        if frm == to:
            cnt += 1
        else:
            visited[frm] = True
            for i in range(n + 1):
                if graph[frm][i] == 0:
                    continue
                else:
                    if visited[i]:
                        continue
                    else:
                        cnt = DFS(i,to,cnt)
                        visited[frm] = False
        return cnt
    real1 = DFS(frm,toss,0)
    visited = [False] * (n + 1)
    real2 = DFS(toss,to,0)
    print(real1)
    print(real2)
    return real1*real2 % 10007

print(solution("SEOUL","DAEGU","YEOSU",[["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))

# 쿠팡 3번

from bisect import bisect_left,bisect_right

def count_by_range(a,left,right):
    right_index = bisect_right(a,right)
    left_index = bisect_left(a,left)
    return right_index - left_index

def solition(k,score):
    arr=[]
    real = []
    for i in range(0,len(score)-1):
        arr.append(score[i]-score[i+1])
        real.append([score[i]-score[i+1],i,i+1])
    arr.sort()
    real.sort()
    e = set(map(int,arr))
    many = arr[-1] - arr[0] + 1
    king = set()
    for i in e:
        a = count_by_range(arr,i,i)
        if a >= k:
            frm = bisect_left(arr, i)
            to = bisect_right(arr, i)
            for i in range(to-frm):
                a,b,c = real[frm+i]
                king = king | {b,c}
    return len(score) - len(list(king))

print(solition(2,[1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))

aa = 3**-7
bb = 3**-8
cc = 3**-9
a = ((2/3)**9)*((6435)*aa+(12870)*bb+(24310)*cc)
print(a)'''


#애플워치 통계량 만들기

'''white = [7,8,5,7,8,3,8.5,5]
black = [9.5,5,8,4,7,7,8.5,7.5]

a = 0
b = 0
for i in range(len(white)):
    a += white[i]
    b += black[i]
mean_white = a/8
mean_black = b/8
var_white = 0
var_black = 0
for i in range(len(white)):
    var_white += (white[i] - mean_white)**2
    var_black += (black[i] - mean_black)**2
var_white /= 8
var_black /= 8
score_white = (10 - mean_white)**2 + var_white
score_black = (10 - mean_black)**2 + var_black
print(mean_black,var_black)
print(mean_white,var_white)
print("하얀색 점수 : ",10 - abs(10 - score_white))
print("검은색 점수 : ",10 - abs(score_black - 10))'''

'''def pibo(i):
    a = 1
    b = 1
    for k in range(2,i):
        c = a
        a = b
        b = c + b
    print(b)

pibo(3032)'''


'''7. numCount([1, 1, 2]) == 2 가 되는 numCount 함수를 구현하시오. (15점)'''

'''def numCount(Array) :
    return len(set(Array))'''

'''함수실행'''
'''print(numCount([1,1,2]))'''

'''a,b  = map(int,input().split())
c = {}
c[str(a)] = b'''


'''def solution(grades, weights, threshold):
    real = {"A+":10,"A0":9,"B+":8,"B0":7,"C+":6,"C0":5,"D+":4,"D0":3,"F":0}
    answer = 0
    for i in range(len(grades)):
       answer += real[grades[i]] * weights[i]
    answer -= threshold
    return answer'''


'''def solution(s, op):
    li = list(str(s))
    answer = []
    if op == "+" :
        for i in range(len(li)-1):
            a = int(''.join(li[:i+1]))
            b = int(''.join(li[i+1:]))
            answer.append(a+b)
    elif op == "-":
        for i in range(len(li)-1):
            a = int(''.join(li[:i+1]))
            b = int(''.join(li[i+1:]))
            answer.append(a-b)
    elif op == "*":
        for i in range(len(li)-1):
            a = int(''.join(li[:i+1]))
            b = int(''.join(li[i+1:]))
            answer.append(a*b)
    return answer'''

'''def solution(money, expected, actual):
    answer = money
    bating = 100
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            answer += bating
            bating = 100
        else :
            answer -= bating
            if bating*2 < answer:
                bating *= 2
            else :
                bating = answer
    print(answer)
    return answer
solution(1000,['H', 'T', 'H', 'T', 'H', 'T', 'H'],['T', 'T', 'H', 'H', 'T', 'T', 'H'])'''

'''def solution(penter, pexit, pescape, data):
    a = [penter,pexit,pescape]
    chunck = []
    answer = ''
    answer += penter
    for i in range(int(len(data)/int(len(penter)))):
        what = data[int(len(penter))*i:int(len(penter))*(i+1)]
        if what in a:
            answer += pescape+what
        else:
            answer += what
    answer += pexit
    return answer
#chunck.append(data[int(len(penter))*i:int(len(penter))*(i+1)])
    print(answer)
solution("123","4","5","123456789123")'''

'''from itertools import combinations

def solution(logs):
    people = set()
    king = {}
    answer = set()
    for i in range(len(logs)):
        a,b,c = logs[i].split()
        people.add(a)
    for i in list(people):
        king[i] = {}
    for i in range(len(logs)):
        a,b,c = logs[i].split()
        king[a][b] = int(c)
    permute = combinations(king, 2)
    for i in list(permute):
        a,b = i
        if king[a] == king[b] and len(king[a]) > 4 :
            answer.add(a)
            answer.add(b)
    if list(answer) == []:
        answer.add("None")
    return list(answer)

solution(["1901 10 50", "1909 10 50"])'''


'''def solution(n, horizontal):
    whereUare =[0,0]
    answer = [[0]*n for i in range(n)]
    value = 0
    # whereuare[0] = 세로, whereuare[1] = 가로
    answer[whereUare[0]][whereUare[1]] = value

    direction = True
    half = False

    while True:
        print(value)

        if horizontal:
            
            if whereUare[0] == 0:
                horizontal = not horizontal
                whereUare[1] += 1
                value += 1
                answer[whereUare[0]][whereUare[1]] = value
                if whereUare == [n - 1, n - 1]: break
            else:
                whereUare[1] -= 1
                whereUare[0] += 1
                value += 2
                answer[whereUare[0]][whereUare[1]] = value
        else:
            if whereUare[1] == 0:
                whereUare[0] += 1
                value += 1
                answer[whereUare[0]][whereUare[1]] = value
                if whereUare == [n - 1, n - 1]: break
                horizontal = not horizontal
            else:
                whereUare[0] -= 1
                whereUare[1] += 1
                value += 2
                answer[whereUare[0]][whereUare[1]] = value
    print(answer)
    return answer'''


'''def solution(n, horizontal):
    answer = [[0]*n for i in range(n)]
    coco = [0,0]
    answer[0][0] = 0
    value = 0

    a = 0
    for i in range(n**2-1):
        #처음결정
        if coco == [n-1,n-1]:
            break
        if 0 in coco or n-1 in coco:
            if horizontal :
                if coco[1] == n-1:
                    coco[0] += 1
                    value += 1
                    answer[coco[0]][coco[1]] = value
                    if a == 0:
                        horizontal = not horizontal
                        a+=1
                else:
                    coco[1] += 1
                    value += 1
                    answer[coco[0]][coco[1]] = value
                coco[0] += 1
                coco[1] -= 1
                value += 2
                answer[coco[0]][coco[1]] = value
            else:
                if coco[0] == n-1:
                    coco[1] += 1
                    value += 1
                    answer[coco[0]][coco[1]] = value
                    if a == 0:
                        horizontal = not horizontal
                        a+=1
                else:
                    coco[0] += 1
                    value += 1
                    answer[coco[0]][coco[1]] = value
                coco[0] -= 1
                coco[1] += 1
                value += 2
                answer[coco[0]][coco[1]] = value
        else:
            if horizontal:
                coco[0] -= 1
                coco[1] += 1
                value += 2
                answer[coco[0]][coco[1]] = value
            else:
                coco[0] += 1
                coco[1] -= 1
                value += 2
                answer[coco[0]][coco[1]] = value
    print(answer)
solution(4,True)'''

'''def solution(n, board):
    answer = 0
    where = {}
    pivot = int(n/2)
    for i in range(n):
        for j in range(n):
            where[board[i][j]] = [i,j]
    start = board[0][0]
    for i in range(n**2):
        if i == 0 :
            c = [abs(a-b) for a,b in zip(list(where[start]),list(where[1]))]
        else:
            c = [abs(a-b) for a,b in zip(where[i],where[i+1])]
        for i in range(len(c)):
            if c[i] > pivot:
                c[i] = n - c[i]
        answer += sum(c) + 1
    return answer
    solution(4,[[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]])'''

# 정수 삼각형

'''a = int(input())
b = [0 for i in range(a)]
c = []
for i in range(a):
    c.append([-1]*(i+1))
    b[i] = list(map(int,input().split()))
result = []
print(c)
#layer층에서 front위치에서 수행한다면?'''
'''def who_is_best(front, layer):

    if layer == 1:
        return b[0][0]

    if c[layer-1][front-1] != -1:
        return c[layer-1][front-1]

    else:
        if front == 1:
            c[layer-1][0] = b[layer-1][0] + who_is_best(front, layer-1)
        elif front == layer:
            c[layer-1][layer-1] = b[layer-1][layer-1] + who_is_best(layer-1, layer-1)
        else:
            c[layer-1][front-1] = b[layer-1][front-1] + max(who_is_best(front-1,layer-1),who_is_best(front,layer-1))

        return c[layer-1][front-1]

for i in range(a):
    result.append(who_is_best(i+1,a))'''

# 퇴사
a = []
c = int(input())
b = [0] * (c)
max_value = 0

for i in range(c):
    a.append(list(map(int,input().split())))

for i in range(c-1,-1,-1):

    # 기간안에 끝나는 일
    if i+a[i][0] <= c-1 :
        b[i] = max(b[i+a[i][0]]+a[i][1],max_value)
        max_value = b[i]
    else:
        b[i] = max_value

print(b)





