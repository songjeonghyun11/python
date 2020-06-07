#Series와 DataFranme의 데이터 확인
# import pandas as pd
# fruits = {"orange":2, "banana": 3}
# print(pd.Series(fruits))

# import pandas as pd
# data = {"fruits:" ["apple", "orange", "banana", "strawberry",
# "kiwifruit"],
#         "year": [2001, 2002, 2001, 2008, 2006],
#         "time": [1,4,5,6,3]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd 
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# data = [10, 5, 8, 12, 3]

# series = pd.Series(data, index=index)

# data = {"fruits": ["apple", "orange", "banana", "strawberry",
# "kiwifruit"],
#         "year": [2001, 2002, 2001, 2008, 2006],
#         "time": [1,4,5,6,3]}
# df = pd.DataFrame(data)

# print("Series 데이터")
# print(series)
# print("\n")
# print("DataFrame 데이터")
# print(df)

#Series 생성
# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index = index)
# print(series)

#참조
# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index = index)
# items1 = series[1:4]
# items2 = series[["apple", "banana", "kiwifruit"]]
# print(items1)
# print(items2)

# #데이터와 인덱스 추출
# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index = index)

# series_values = series.values
# series_index =series.index
# print(series_values)
# print(series_index)

#요소 추가 삭제, 필터링
# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index = index)
# pineapple = pd.Series([12], index=["pineapple"])
# #series = series.append(pineapple)
# #series = series.drop("straberry")
# Conditions = [True, True, False, False, False]
# print(series[Conditions])
#series = series[series >= 5][series < 10]

#정렬
import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index = index)
# items1 = series.sort_index()
# items2 = series.sort_values()

#DataFrame 생성
# data = {"fruits": ["apple", "orange", "banana", "strawberry",
# "kiwifruit"],
#         "year": [2001, 2002, 2001, 2008, 2006],
#         "time": [1,4,5,6,3]}
# df = pd.DataFrame(data)
# print(df)

# #인덱스와 칼럼설정(행추가,열추가)
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data1 = [10, 5, 8, 12, 3]
# data2 = [30,25,12,10,8]
# series1 = pd.Series(data1, index = index)
# series2 = pd.Series(data2, index = index)
# df = pd.DataFrame([series1, series2])
# df.index = [1,2]
# df = df.append(series2, ignore_index=True)
# new_column = pd.Series([15, 7], index = [0,1])
# df["mangd"] = new_column
# print(df)

#데이터 참조
# import numpy as np
# np.random.seed(0)
# columns = ["apple", "orange", "banana", "strawberry","kiwifruit"]
# #         "year": [2001, 2002, 2001, 2008, 2006],
# #         "time": [1,4,5,6,3]}
# df = pd.DataFrame()
# for column in columns:
#     df[column] = np.random.choice(range(1, 11), 10)
# df.index = range(1, 11)
# df = df.loc[range(2,6), ["banana","kiwifriut"]]
# #df = df.loc[[1,2],["time", "year"]]
# print(df)

#행 또는 열 삭제
# data = {"fruits": ["apple", "orange", "banana", "strawberry",
# "kiwifruit"],
#         "year": [2001, 2002, 2001, 2008, 2006],
#         "time": [1,4,5,6,3]}

# df = pd.DataFrame(data)
# df_1 = df.drop(range(0,2))

# df_2 = df.drop("year", axis =1)
# print(df_1)

# import numpy as np
# np.random.seed(0)
# columns = ["apple", "orange", "banana", "strawberry","kiwifruit"]

# df = pd.DataFrame()
# for column in columns:
#     df[column] = np.random.choice(range(1, 11), 10)
# df.index = range(1, 11)
# df = df.drop(np.arange(2,11,2))
# df = df.drop("strawberry", axis=1)
# #정렬
# df = df.sort_values(by="year", ascending=True)

#연습문제!
import pandas as pd
import numpy as np

index = ["growth", "mission", "ishikawa", "pro"]
data = [50, 7, 26, 1]

series = pd.Series(data, index =index)
aidemy = series.sort_index()

aidemy1 = pd.Series([30], index=["tutor"])
aidemy2 = series.append(aidemy1)

df = pd.DataFrame()
for index in index:
    df[index] = np.random.choice(range(1,11), 10)
    df.index = range(1,11)

aidemy3 = df.loc[range(2,6), ["ishikawa"]]
print()
print(aidemy3)
