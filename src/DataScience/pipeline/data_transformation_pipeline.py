from src.DataScience.components.data_transformation import DataTransformation
from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience import logger
from pathlib import Path

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def transform_data(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
                if status =="True":
                        # initialize the configuration manager class
                        config_manager = ConfigurationManager()
                        # get the data transformation config method from the configuration manager class
                        data_transformation_config = config_manager.get_data_transformation_config()
                        # initialize the data transformation class and giving the data transformation config as input
                        data_transformation = DataTransformation(config=data_transformation_config)
                        # Here we are calling the train_test_split method from the data transformation class
                        data_transformation.train_test_split()
                else:
                     raise Exception("Your data is not validated")
        except Exception as e:
             raise e
                    


if __name__ == '__main__':
    logger.info('Data transformation pipeline started')
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.transform_data()
    logger.info('Data transformation pipeline ended')