import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib as jl


class Trainer:
    def __init__(self, model):
        self.model = model
        self.df = pd.DataFrame() # empty df

        self.train()

    def get_train_data(self):
        newest_data = pd.read_csv('data/train_preprocessed.csv')

        X = newest_data.iloc[:,1:]
        y = newest_data.iloc[:,0]

        # retrain only if dataframe has changed or if there is no model
        if (self.df.empty or not self.model or not self.df.equals(newest_data)):
            self.df = newest_data
            return X, y

        # return empty dfs if there is no need to train
        return pd.DataFrame(), pd.DataFrame()



    def train(self):
        X, y = self.get_train_data()

        if (X.empty and y.empty):
            return False # no training

        # train model
        if (not self.model):
            self.model = RandomForestClassifier(max_depth=2, random_state=0)

        self.model.fit(X, y)
        print('----- finish training -----')

        # save model
        jl.dump(self.model, 'model/model.joblib')

        return True

    def predict(self, data):
        return self.model.predict(data)


