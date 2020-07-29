import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

test = pd.read_csv('./upload/test2.csv')
train = pd.read_csv('./upload/train2.csv')

train = train.fillna(0)
test= test.fillna(0)
target = 'SeriousDlqin2yrs'
X = train.drop([target],axis=1).values
y = test[target].values
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
clf.score(X_test, y_test)

pred = clf.predict(X_test)
csv_pred = pd.DataFrame({'Prediction' : pred})
csv_pred.to_csv('test2-predictions.csv', index=False)
