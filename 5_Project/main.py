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

def right(total_l, key_l, lock_l, mother_matrix, ans):
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

    while True:
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

        # 확인작업맞으면!
        if right(total_l,key_l,lock_l,mother_matrix,0):
            return True
        else:
        # 확인작업틀리면 이동작업!
            for i in range(a,key_l+a):
                for j in range(b,key_l+b):
                    #   print("i",i,"j",j,"i-a",i-a,"j-b",j-b)
                    mother_matrix[i][j] -= key[i-a][j-b]
                    mother_matrix[i][j+1] += key[i-a][j-b]
            b += 1
            if key_l+b > total_l-1 : a += 1;b = 0
            if key_l+a > total_l-1 :
        #이동작업도 안되면 회전작업
                key = tilt_it(key)
                c += 1
                a = 0
                b = 0
        #회전을 다했음에도 안되면 안열리는것이다.
            if c == 4: return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))