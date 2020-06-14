#14.1.1 pandas로 csv읽기

import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
#각 수치가 무엇을 나타내는지 컬럼 헤더를 추가합니다.
df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols",
            "Proanthocyanins", "Color intensity", "Hue", "0D280/0D315 of diluted wines", "Proline"]
df

#14.1.2 csv 라이브러리로 csv만들기
import csv

#with 문을 사용해서 파일을 처리
with open("csv0.csv", "w") as csvfile:
    # writer() 메서드의 인수로 csvfile과 개행 코드(\n)를 지정합니다.
    writer = csv.writer(csvfile, lineterminator="\n")

    #writerow(리스트)로 행을 추가합니다.
    writer.writerow(["city", "year", "season"])
    writer.writerow(["Nagano", "1998", "winter"])
    writer.writerow(["Sydney", "2000", "summer"])
    writer.writerow(["Salt Lake City", "2002", "winter"])
    writer.writerow(["Athens", "2004", "summer"])
    writer.writerow(["Torino", "2006", "winter"])
    writer.writerow(["Beijing", "2008", "summer"])
    writer.writerow(["Vancouver", "2010", "winter"])
    writer.writerow(["London", "2012", "summer"])
    writer.writerow(["Sochi", "2014", "winter"])
    writer.writerow(["Rio de Janeiro", "2016", "summer"])


#14.1.3 pandas로 csv만들기
import pandas as pd

data = {"city": ["Nagano", "Sydney", "Salt Lake City", "Athens", "Torino",
        "Beijing", "Vancouver", "London", "Sochi", "Rio de Janeiro"],
        "year": [1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
        "season": ["winter", "summer", "winter", "summer", "winter", "summer", "winter",
        "summer", "winter", "summer"]}

df = pd.DataFrame(data)
df.to_csv("csv1.csv")

