import os
import pandas as pd
from src.DataScience import logger
from sklearn.model_selection import train_test_split
from src.DataScience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # lets seperate the data into train and test and save him into csv
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        train,test = train_test_split(data,test_size=0.2,random_state=42)

        # saving into csv
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('train and test data saved successfully')
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)