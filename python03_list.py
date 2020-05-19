# 자료형
#1. 리스트

a = [1,2,3,4,5]
b = [1,2,3,'a','b']
print(b)

print(a[0] + a[3])
#print(b[0] + b[3])
print(type(a))
print(a[-2])
print(a[1:3])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[1])
print(a[-1])
print(a[-1][1]) #-1인덱스 안의 리스트 안에 [1]번째 데이터

#1-2. 리스트 슬라이싱
a = [1,2,3,4,5]
print(a[:2])

#1-3. 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b) #숫자의더하기로 출력하고싶으면 numpy

c = [7,8,9,10]
print(a + c)
print(a * 3)

#print(a[2] + 'hi') 타입에러
print(str(a[2])+'hi')

f = '5'
print(a[2] + int(f) )

#리스트 관련 함수
a = [1, 2, 3]
a.append(4) #리스트에 삽입
print(a)

#a = a.append(5) 오류(삽입문은 따로 작성)

a = [1, 3, 4, 2]
a.sort()
print(a)

a.reverse()
print(a)

print(a.index(3)) # == a[3]
print(a.index(1)) # == a[1]

a.insert(0, 7)
print(a)
a.insert(3, 3)
print(a)
a.remove(7)
print(a)
a.remove(3)
print(a)
