from src.DataScience.entity.config_entity import DataValidationConfig
import pandas as pd

# Helper function to read the config file and then check the data validation
class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config
# function to validate the data if it presents in the schema
    def validate_all_columns(self)-> bool:
        try:
            validate_status = None
            data = pd.read_csv(self.config.unzipped_data)

            all_columns = list(data.columns)
            all_schema = self.config.all_shema.keys()
# Here i am checking if the columns in the data is present in the schema
            for col in all_columns:
                if col not in all_schema:
                    validate_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation Failed {validate_status}")
                else:
                    validate_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation Passed {validate_status}")
            return validate_status
        except Exception as e:
            raise e
