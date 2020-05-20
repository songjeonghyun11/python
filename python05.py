05:#3. 딕셔너리 # 중복 X
# {키 : 벨류}
# {key : value}

a = {1: 'hi',
     2: 'Hello'}

print(a)
print(a[2])

b = {'hi': 1, 'hello': 2}
print(b['hi']) # 키와 벨류가 똭똭 자리가 있음
print("===========================================================")

# 딕셔너리 요소 삭제

del a[1]
print(a)
del a[2]
print(a)

a = {1: 'a', 1: 'b', 1:'c'} 
# 1에 처음에는 a가 다음 b가 다음 c가 들어가서 출력은 c
print(a)

b = {1: 'a', 2:'a', 3:'a'}
print(b)
print("===========================================================")

a = {'name' : 'yun', 'phone': '010', 'birth': '0511'}
print(a.keys())
print(a.values())
print(type(a))
print(a.get('name'))
print(a['name'])
print(a.get('phone'))
print(a['phone'])
print("===========================================================")
