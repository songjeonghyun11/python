06: # # for문 반복문
# a = {'name' : 'yun', 'phone': '010', 'birth': '0511'}

# for i in a.keys():
#     print(i)

# a = [1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     i = i*i
#     print(i)
# print('melong')

# for i in a :
#     print(i)
# print("===========================================================")

# # while문
# '''
# while 조건문 : # 참일 동안 계속 돈다.
#     수행할 문장
# '''
# print("===========================================================")

# # if문

# if 1 :
#     print('True')
# else:
#     print('False')

# if 3:
#     print('True')
# else:
#     print('False')

# if 0:
#     print('True')
# else:
#     print('False')
# if -1:
#     print('True')
# else:
#     print('False')
# print("===========================================================")

'''
비교 연산자
<, >, ==, !=, >=, <=
'''
# == 같니? 하고 물어보는거 != 아니지?!
# a = 1
# if a == 1:
#     print('출력잘되')

# money = 10000
# if money >= 30000:
#     print('한우가자')
# else:
#     print('라면먹자ㅜ')
# print("===========================================================")

# and, or, not 
# and  = 1 : 1 그래야 출력

# or = 1 : 0
#      0 : 1 한쪽만 참이어도 출력

# not 아니야!!!

# money = int(input())
# card = int(input())
# if money >= 30000 or card ==1:
#     print('한우가즈아')
# else:
#     print('라면먹자')          
# print("===========================================================")


jumsu = [90, 25, 67, 45, 80]
number = 0
# for i in jumsu:
#     if i >= 60:
#         print("경] 합격 [축")
#         number = number + 1
        
# print("합격인원: ", number, "명")
# print("===========================================================")

# # break
# for i in jumsu:
#     if i < 30:
#         break
#     elif i >= 60:
#         print("경] 합격 [축")
#         number = number + 1
        
# print("합격인원: ", number, "명")
# print("===========================================================")

# continue
for i in jumsu:
    if i < 60:
        continue
    elif i >= 60:
        print("경] 합격 [축")
        number = number + 1
        
print("합격인원: ", number, "명")
