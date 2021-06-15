#2675 문자열 반복

# n = int(input())
# answer = []
# for i in range(n):
#     n,m = input().split(' ')
#     m = list(m)
#     new = []
#     for i in m:
#         for j in range(int(n)):
#             new.append(i)
#     answer.append(''.join(new))
#
# for i in answer:
#     print(i)

#2920 음계

# target = '12345678'
# revers = ''.join(list(target)[::-1])
#
# a = ''.join(list(input().split()))
#
# if target in a and revers not in a :
#     print("ascending")
# elif revers in a and target not in a:
#     print("descending")
# else:
#     print('mixed')

#10809 알파벳 찾기

# target = input()
#
# answer = []
#
# for i in range(26):
#     if chr(97+i) in target:
#         answer.append(str(target.index(chr(97+i))))
#     else:
#         answer.append('-1')
#
# print(' '.join(answer))

#10809 상수

# n,m = input().split()
# n = int(''.join(list(n)[::-1]))
# m = int(''.join(list(m)[::-1]))
#
# if n > m :
#     print(n)
# else:
#     print(m)

#2475 검증수

# li = input().split()
#
# answer = 0
#
# for i in li:
#     answer += int(i)**2
#
# print(answer%10)

#1152 단어의 갯수

# print(len(list(input().split())))

#1157 단어 공부

# word = list(input().lower())
# all = {i:0 for i in set(word)}
# for i in word:
#     all[i] += 1
# all = sorted(all.items(),key=(lambda x:x[1]),reverse=True)
#
# maximum = all[0][1]
#
# if [i[1] for i in all].count(maximum) > 1:
#     print('?')
# else:
#     print(all[0][0].upper())


