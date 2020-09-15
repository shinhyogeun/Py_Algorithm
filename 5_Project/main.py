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
answer = 1
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
        break

# 5.볼링공 고르기

'''n,m = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] != arr[j]:
          answer += 1
print(answer)'''

# 무지의 먹방 라이브~




