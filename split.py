import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('upload/cs-training.csv', index_col=0)

train2, test2 = train_test_split(data, test_size=0.50, random_state=42)

train2.to_csv('upload/train2.csv')
test2.to_csv('upload/test2.csv')