import joblib
import os
import pandas as pd
from sklearn.metrics import r2_score
dir = './dataset'
df = pd.read_csv(os.path.join(dir, "train.csv"))

# count column을 최대 100으로 clip 후 정규화
df["count"] = df["count"].clip(upper=100)
df["count"] = df["count"].apply(lambda x: (x-1)/(100-1))

print(df["count"].mean())