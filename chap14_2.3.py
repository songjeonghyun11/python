# #DataFrame 복습

# import pandas as pd
# from pandas import Series, DataFrame

# attri_data1 = {"ID": ["100","101", "102", "103", "104","106","108","110","111","113"],
#                 "city":["서울","부산","대전","광주","서울","서울","부산","대전","광주","서울"],
#                 "birth_year":[1990,1989,1992,1997,1982,1991,1988,1990,1995,1981],
#                 "name": ["영이", "순돌", "짱구", "태양","션","유라","현아","태식","민수","호식"]}

# attri_data_frame1 = DataFrame(attri_data1)

# attri_data2 = {"ID":["107", "109"],
#                 "city": ["봉화", "전주"],
#                 "birth_year": [1994,1988]}
# attri_data_frame2 = DataFrame(attri_data2)
# #행추가, 정렬,행번호 매기기
# attri_data_frame1.append(attri_data_frame2).sort_values(by="ID",
# ascending=True).reset_index(drop=True)

#14.3 결측지
import numpy as np
from numpy import nan as NA
import pandas as pd
sample_data_frame = pd.DataFrame(np.random.rand(10,4))

#일부 데이터 누락시키기
sample_data_frame.iloc[1, 0] = NA
sample_data_frame.iloc[2, 2] = NA
sample_data_frame.iloc[5:, 3] = NA

sample_data_frame

#nan 가진행 통째로 삭제
sample_data_frame.dropna()
#결손이 적은 열만 남기기
sample_data_frame[[0,1,2]].dropa()


#14.3.2 결측치 보완
import numpy as np
from numpy import nan as NA
import pandas as pd
sample_data_frame = pd.DataFrame(np.random.rand(10,4))

#일부 데이터 누락시키기
sample_data_frame.iloc[1, 0] = NA
sample_data_frame.iloc[2, 2] = NA
sample_data_frame.iloc[5:, 3] = NA

sample_data_frame

sample_data_frame.fillna(0)
sample_data_frame.fillna(method="ffill")


#14.3.3. 결측치 보완(평균값 대입법)
import numpy as np
from numpy import nan as NA
import pandas as pd
sample_data_frame = pd.DataFrame(np.random.rand(10,4))

#일부 데이터 누락시키기
sample_data_frame.iloc[1, 0] = NA
sample_data_frame.iloc[2, 2] = NA
sample_data_frame.iloc[5:, 3] = NA

sample_data_frame.fillna(sample_data_frame.mean())
