from src.DataScience.constants import *
from src.DataScience.utils.common import read_yaml, create_directories
from src.DataScience.entity.config_entity import DataIngestionConfig, DataValidationConfig

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
    


    