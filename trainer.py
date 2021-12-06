import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
import joblib as jl
import os.path


class Trainer:
    def __init__(self):
        self.model = None

    def train(self, X, y):
        print('X: ' + str(X) + ' y: ' + str(y))
        # load model if it exists
        if (os.path.isfile('model/model.joblib')):
            self.model = jl.load('model/model.joblib')

        if (not X or not y):
            return False # no training

        # train model
        if (not self.model):
#            self.model = RandomForestClassifier(max_depth=2, random_state=0)
            self.model = linear_model.SGDClassifier()

        self.model.partial_fit(X, [y], classes=[0, 1])

        # save model
        jl.dump(self.model, 'model/model.joblib')

        return True

    def predict(self, data):
        print(str(data))
        return self.model.predict(data)


