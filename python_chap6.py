#함수 기초

# vega = "potato"
# n = [4,5,2,7,6]

# print(len(n))
# print(len(vega))

# city = "Tokyo"
# print(city.upper())
# print(city.count("o")) # o가 몇개 들어갔나 count

# animal = "elephant"
# animal_big = animal.upper()
# print(animal_big)
# print(animal.count("e"))

# fruit = "바나나"
# color = "노란색"
# print("{} 는 {}색 입니다.".format(fruit, color))

# n = [3,6,8,6,3,2,4,6]
# print(n.index(2))
# print(n.count(6))

# list = [1, 10, 2, 20]
# list.sort()
# list2 = list.reverse()
# print(list)
# print(list2)

# n = [53, 26, 37, 69, 24, 2]
# n.sort()
# print(n)
# n.reverse()
# print(n)

# #함수

# def sing():
#     print("노래합니다.")
# sing()

# def introduce():
#     print("홍길동 입니다")
# introduce()

# def cube_cal(n):
#     print(n**3)
# cube_cal(3)

# def introduce(n, age):
#     print(n + "입니다." + str(age) + "살입니다" )
# introduce("홍길동" , 25)

# def introduce(age, n = "홍길동" ):
#     print(n + "입니다." + str(age) + "살입니다")
# introduce(18)

# def introduce(first = "김", second = "길동"):
#     return "성은" + first + "이고, 이름은" + second + "입니다."
# print(introduce("홍"))

# from time import time
# now_time = time()
# print(now_time)

class MyProduct:
    def __init__(self, name, price):

        self.name = name
        self.price = price
        self.stock = 0
        self.sales = 0

product1 = MyProduct("cake", 500)
