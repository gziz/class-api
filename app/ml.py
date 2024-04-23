import pickle

import numpy as np


class KMeans:

    def __init__(self, model_path):

        with open(model_path, "rb") as file:
            self.kmeans = pickle.load(file)

    def predict(self, data):
        arr = np.expand_dims(np.array(data), 0)
        pred = self.kmeans.predict(arr)
        return int(pred[0])
