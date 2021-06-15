# Seciotn04-4

# 리스트는 (순서0,중복0,수정0,삭제0)

a = []
b = list()
c = [1,2,3,4]
d = [10,100,'Pen','asd']

#인덱싱

print(c+d)
print(c*2)

#리스트 수정, 삭제
c[1:2] = [100,1000,10000]
print(c)
c[1] = ['a','b','c']

print()
print()
print()

#리스트 수정, 삭제
y = [5,2,3,1,4]
y.append(6)
y.sort()
y.reverse()
y.insert(2,7)
y.remove(2)
ex=[99,77]
y.extend(ex)

#튜플 (순서0,중복0,수정x,삭제x)
a = ()
b = (1,)
c = (1,2,3,4)

#튜플함수
z = (5,2,1,3)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(3))

print()
print()
print()
print()
print()

#딕셔너리 (순서x,중복x,수정0,삭제0)

#key,vlaue(JSON) -> MongoDB
#선언
a = {'name':'Kim','phone':'010-777-777', 'birth':'870214'}

print(a.get('asd'))

#집합!

#교집합
s1 = set([1,2,3,4])
s2 = set([1,2,3,4])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1-s2)
print(s1.difference(s2))

s2.add(2)
s2.remove(2)




