from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.Model_evaluation import ModelEvaluation
from src.DataScience import logger
import os
os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/YOURNAME/datascience.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'YOUR NAME'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'YOUR PASSWORD' 

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config_manager = ConfigurationManager()
        model_eval_config = config_manager.get_model_eval_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.log_into_mlflow()

if __name__ == '__main__':
    logger.info('Model evaluation pipeline started')
    model_eval_pipeline = ModelEvaluationPipeline()
    model_eval_pipeline.initiate_model_evaluation()
    logger.info('Model evaluation pipeline completed')