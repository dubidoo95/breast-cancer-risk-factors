import warnings
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import  PolynomialFeatures, OneHotEncoder
from sklearn.pipeline import make_pipeline

warnings.filterwarnings(action='ignore')

# dataset 불러오기
dir = './dataset/'
df = pd.read_csv(dir + "train.csv")

# count column을 최대 100으로 clip 후 정규화
df["count"] = df["count"].clip(upper=100)
df["count"] = df["count"].apply(lambda x: (x-1)/(100-1))

# features, target 정의
features = df.drop(columns='count').columns
target = 'count'

# features, target 나누기
X_train, y_train = df[features], df[target]

# polynomial linear regression model
def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(
                        OneHotEncoder(),
                        PolynomialFeatures(degree), 
                        LinearRegression(**kwargs))
poly = PolynomialRegression(degree=2)
poly.fit(X_train, y_train)
y_pred = poly.predict(X_train)

joblib.dump(poly, './flask_app/project3_model.pkl')