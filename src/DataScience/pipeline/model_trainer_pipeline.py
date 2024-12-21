from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.Model_trainer import ModelTrainer
from src.DataScience import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config_manager = ConfigurationManager()
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == '__main__':
    logger.info('Model training pipeline started')
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.initiate_model_trainer()
    logger.info('Model training pipeline completed')