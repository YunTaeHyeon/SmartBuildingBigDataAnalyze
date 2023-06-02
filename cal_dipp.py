#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

# CSV 파일을 데이터프레임으로 읽어오기
df = pd.read_csv('/Users/dongh/competition DATA/train_data.csv', encoding='cp1252')

df = df.rename(columns={'Àç½ÇÀÎ¿ø': 'person'})

# 새로운 데이터프레임 생성
new_df = pd.DataFrame()

# 각 열에 대해 전 행과의 차이 계산하여 새로운 열 생성
for column in df.columns[1:4]:
    # 첫 번째 행은 NaN으로 처리
    new_df[column + '_dipp'] = [None] + list(df[column].diff()[1:])

# 결과 출력
print(new_df)


# In[ ]:




