from src.DataScience.constants import *
from src.DataScience.utils.common import read_yaml, create_directories, save_json
from src.DataScience.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig

# building configuration manager
class ConfigurationManager:
    def __init__(self,
                 config_file_path= CONFIG_FILE_PATH,
                 params_file_path= PARAMS_FILE_PATH,
                 shema_file_path= SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(shema_file_path)

        # Lets create directiories
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        # Here i am taking the data ingestion configuration from the config file ( which is a yaml file)
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        # Here i am making an object of DataIngestionConfig class and passing the values from the config file
        data_ingestion = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
        return data_ingestion
    # Here i am creating a function to get the data validation configuration
    def get_data_validation_config(self):
        config = self.config.data_validation
        schema = self.schema.COLUMN
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzipped_data=config.unzipped_data,
            all_shema=schema
        )
        return data_validation_config
    # This is the functon to get the data transformation configuration
    def get_data_transformation_config(self):
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
    # This is the function to get the model trainer configuration
    def get_model_trainer_config(self):
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )
        return model_trainer_config
    
    def get_model_eval_config(self):
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            mlflow_uri='https://dagshub.com/hamzajamil4000/datascience.mlflow'
        )
        return model_evaluation_config
    


    