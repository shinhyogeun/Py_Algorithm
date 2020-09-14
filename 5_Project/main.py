# 모험가 길드

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

# 곱하기 혹은 더하기

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

x = 0
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
print("세타가 0.9이면 ",((1/9)*(0.9)**3*(0.1)**2)/0.0167)

