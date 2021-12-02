import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib as jl

def get_train_data():
    df = pd.read_csv('data/train_preprocessed.csv')

    X = df.iloc[:,1:]
    y = df.iloc[:,0]

    return X, y


def train():
    X, y = get_train_data()

    # train model
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X, y)

    # save model
    jl.dump(clf, 'model/clf.joblib')


train()
