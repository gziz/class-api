import pickle

import numpy as np


class KMeans:
    def __init__(self, model_path):
        with open(model_path, "rb") as file:
            self.kmeans = pickle.load(file)
        # Orden de variables en entrenamiento
        self.feature_order = ['fix_acid', 'vol_acid', 'cit_acid', 'res_sugar', 'chlor', 'free_sulf', 'tot_sulf', 'dens', 'pH', 'sulph', 'alc', 'qual']

    def predict(self, data):
        ordered_data = [data[feature] for feature in self.feature_order]
        arr = np.array([ordered_data])
        pred = self.kmeans.predict(arr)
        return int(pred[0])