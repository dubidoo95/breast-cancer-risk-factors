import os
import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터 불러오기
dir = './dataset/'
df = pd.read_csv(dir+"data.csv")

# train, val, test 나누기
train, test = train_test_split(df, train_size=0.8, random_state=42)
train, val = train_test_split(train, train_size=0.8, random_state=42)

# 데이터 저장
train.to_csv("./dataset/train.csv", index=False)
val.to_csv("./dataset/validation.csv", index=False)
test.to_csv("./dataset/test.csv", index=False)