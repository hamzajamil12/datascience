import pandas as pd
import os
from src.DataScience import logger
from sklearn.linear_model import ElasticNet
import joblib

from src.DataScience.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # first lets import data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # lets slpit the train and test according to taget column
        train_x = train_data.drop(columns=[self.config.target_column], axis=1)
        test_x = test_data.drop(columns=[self.config.target_column], axis=1)

        # labels
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        # now lets import and train model
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        model.fit(train_x, train_y)

        # lets save the model
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))  