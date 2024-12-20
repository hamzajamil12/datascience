from src.DataScience.components.data_validation import DataValidation
from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def validate_data(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    logger.info("Data Validation Pipeline Started")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.validate_data()
    logger.info("Data Validation Pipeline Ended")   