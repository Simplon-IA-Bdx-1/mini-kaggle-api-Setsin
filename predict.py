import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sys import path
%matplotlib inline

train = pd.read_csv('./upload/train2.csv')
test = pd.read_csv('./upload/test2.csv')
df = pd.concat([train, test], ignore_index=1)
mask = df['SeriousDlqin2yrs'].notnull()

df = df.drop('Unnamed: 0', axis=1)
