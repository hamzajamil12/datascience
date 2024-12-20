from src.DataScience import logger
from src.DataScience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DataScience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.ingesting_data()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>>>>>>>>Starting {STAGE_NAME}")
    pipeline = DataValidationTrainingPipeline()
    pipeline.validate_data()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    raise e