# Lets import liabrarires for model evaluation
import pandas as pd
import os
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from urllib.parse import urlparse
from pathlib import Path

from src.DataScience.config.configuration import ModelEvaluationConfig
from src.DataScience.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    # eval func
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    # log into mlflow
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # spliting the data
        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]

        # lets set mlflow uri
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # lets run mlflow
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            # lets get the metrics
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            # saving the metrics first local and then into json
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(Path(self.config.metric_file_name), data = scores)

            # lets log the metrics into mlflow
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # model registry does not work with file store
            if tracking_uri_type_store != "file":
                # Register the model
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetWineModel")

            else:
                mlflow.sklearn.log_model(model, "model")
