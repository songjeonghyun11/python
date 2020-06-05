#리스트
# c_list = ['red', 'blue', 'yellow']
# print(c_list)

#n = 3
#print(["사과", n , '고릴라'])

#a = [1,2,3,4]
#print(a[1])
#print(a[3])

#fruits = ["apple", 2 ,"orange", 4, "grape", 3, "banana", 1 ]
#print(fruits[1])
#print(fruits[-1])

# chaos = ["cat", "apple", 2, "orange", 4, "grape", 3, "banan", 1, "elephant", "dog"]
# fruits = [chaos[1:9]]
# print(fruits)

# c = ["dog", "blue", "yellow"]
# c[0] = "red"
# c.append("green")
# print(c)

# c = ["red", "blue", "yellow"]
# c_copy = c
# c_copy[1] = "green"
# print(c_copy)

#딕셔너리
#town = {"경기도":"수원", "서울":"중구"}
#print(town)

# dic = {"Japan": "Tokyo", "Korea": "Soul"}
# dic["Japan"] = "Osaka"
# dic["China"] = "Beijin"
# print(dic)
#del dic["China"]

# while 문
# n = 2
# while n > 0:
#     print(n)
#     n -= 1

# n = 5
# while n != 0:
#     print(n)
#     n -= 1

# x = 5
# while x != 0:
#     if x != 0:
#         print(x)
#         x -= 1

# for 문 
# animals = ["tiger", "dog", "elephant"]
# for animal in animals:
#     print(animal)

# storages = [1,2,3,4,5,6,7,8,9,10]
# for n in storages:
#     print(n)
#     if n >= 5:
#         print("end")
#         break

# storages = [1,2,3,4,5,6]
# for n in storages:
#     print(n)
#     if n == 4:
#         break;

# list = ["a", "b"]
# for index, value in enumerate(list):
#     print(index, value)

# animals = ["tiger", "dog", "elephant"]
# for index, animal in enumerate(animals):
#     print(index, animal)

# fruits = {"strawberry":"red", "peach":"pink", "banana": "yellow"}
# for fruit, color in fruits.items():
#     print(fruit, color)

items = {"지우개": [100,2], "펜": [200, 3], "노트": [400, 5]}
total_price = 0

for item in items:
    print(item + "한 개에" + str(items[item][0])+ "원 이며" + str(items[item][1]) + "개 구입합니다.")
    total_price += items[item][0]*items[item][1]
    print("지불해야할 금액은 : ", str(total_price))
    money = 2000
    if money > total_price:
        print("거스름은" + str(total_price) + "입니다")
    elif money == total_price:
        print("거스름돈은 없습니다")
    else:
        print("돈이 부족합니다")
