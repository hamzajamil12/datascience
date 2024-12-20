from src.DataScience.components.data_ingestion import DataIngestion
from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def ingesting_data(self):
        # Here i am creating an object of ConfigurationManager class
        config_manager = ConfigurationManager()
        # Here i am getting the data ingestion configuration
        data_ingestion_config = config_manager.get_data_ingestion_config()
        # Here i am creating an object of DataIngestion class and passing the data ingestion configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # Here i am downloading the data
        data_ingestion.download_data()
        # Here i am extracting the data
        # data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.ingesting_data()
        logger.info(f"Finished {STAGE_NAME}")
    except Exception as e:
        raise e