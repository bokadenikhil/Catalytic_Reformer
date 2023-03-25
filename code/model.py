#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.ensemble import RandomForestRegressor

import pickle

#Loading Data
path = r'..\src\ccr-data.xlsx'
df = pd.read_excel(path)
df.dropna(inplace=True)
df.drop('State',axis=1,inplace=True)

## Splitting dataset
target_col = ['Reformate RON', ' C5+ RON', 'C6+ RON']
X,y = df.drop(target_col,axis=1), df[target_col]
test_size, random_state = 0.2, 42
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)
y_train = y_train.values
y_test = y_test.values

rf = RandomForestRegressor()
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)

print('R2 Score:', r2_score(y_test,y_pred))

pickle.dump(rf,open(r'..\model\model_v1.pkl','wb'))

