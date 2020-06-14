import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header = None)
df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols",
            "Proanthocyanins", "Color intensity", "Hue", "0D280/0D315 of diluted wines", "Proline"]
print(df["Alcohol"].mean())

#14.4.2 중복 데이터
import pandas as pd
from pandas import DataFrame

dupli_data =DataFrame({"col":[1, 1, 2, 3, 4, 4, 6, 6],
                        "col2":["a", "b","b","b","c","c","b", "b"]})
dupli_data
print(dupli_data)
#중복된 행을 true로 표현
dupli_data.duplicated()
#중복 데이터 삭제
dupli_data.drop_duplicates()

#14.4.3. 매핑
import pandas as pd
from pandas import Series, DataFrame

attri_data1 = {"ID": ["100","101", "102", "103", "104","106","108","110","111","113"],
                "city":["서울","부산","대전","광주","서울","서울","부산","대전","광주","서울"],
                "birth_year":[1990,1989,1992,1997,1982,1991,1988,1990,1995,1981],
                "name": ["영이", "순돌", "짱구", "태양","션","유라","현아","태식","민수","호식"]}

attri_data_frame1 = DataFrame(attri_data1)

attri_data_frame1

city_map = {"서울": "서울",
            "광주": "전라도",
            "부산": "경상도",
            "대전": "충청도"}
city_map
#새로운 칼럼 region을 추가
attri_data_frame1["region"] = attri_data_frame1["city"].map(city_map)
attri_data_frame1

#14.4.4 구간분할
import pandas as pd
from pandas import Series, DataFrame

attri_data1 = {"ID": ["100","101", "102", "103", "104","106","108","110","111","113"],
                "city":["서울","부산","대전","광주","서울","서울","부산","대전","광주","서울"],
                "birth_year":[1990,1989,1992,1997,1982,1991,1988,1990,1995,1981],
                "name": ["영이", "순돌", "짱구", "태양","션","유라","현아","태식","민수","호식"]}

attri_data_frame1 = DataFrame(attri_data1)

#분할 리스트 만들기
birth_year_bins = [1980, 1985, 1990, 1995, 2000]
#구간 분할 실시
birth_year_cut_data = pd.cut(attri_data_frame1.birth_year, birth_year_bins)
birth_year_cut_data
#예시3
pd.value_counts(birth_year_cut_data)
#예시4
group_names = ["first1980", "second1980", "first1990", "second1990"]
birth_year_cut_data = pd.cut(attri_data_frame1.birth_year, birth_year_
bins, label =group_names)
pd.value_counts(birth_year_cut_data)
#예시5
pd.cut(attri_data_frame1.birth_year, 2)

#연습문제
import pandas as pd
import numpy as np
from numpy import nan as NA
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols",
            "Proanthocyanins", "Color intensity", "Hue", "0D280/0D315 of diluted wines", "Proline"]

# 변수df의 상위10행을 변수 df_ten에 대입하여 표ㅕㅅ
df_ten = df.head(10)
print(df_ten)

#데이터의 일부를 누락
df_ten.iloc[1,0] = NA
df_ten.iloc[2,3] = NA
df_ten.iloc[4,8] = NA
df_ten.iloc[7,3] = NA
print(df_ten)

#fillna()메스드를 nan에 평균값 대입
df_ten.fillna(df_ten.mean())
print(df_ten)

print(df_ten["Alcohol"].mean())

#중복된 행을 제거
df_ten.append(df_ten.loc[3])
df_ten.append(df_ten.loc[6])
df_ten.append(df_ten.loc[9])
df_ten = df_ten.drop_duplicates()
print(df_ten)

#Alcohol 열의 구간 리스트 작성
alcohol_bins = [0,5, 10, 15, 20, 25]
alcoholr_cut_data = pd.cut(df_ten["Alcohol"], alcohol_bins)

#구간수를 집계하여 출력하세요
print(pd.value_counts(alcoholr_cut_data))
