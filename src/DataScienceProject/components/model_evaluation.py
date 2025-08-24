import os 
from src.DataScienceProject.entity.config_entity import ModelEvaluationConfig
from sklearn import metrics
import pandas as pd 
import numpy as np
from urllib.parse import urlparse
import joblib
import mlflow
import mlflow.sklearn
from src.DataScienceProject.utils.common import *
from dotenv import load_dotenv

load_dotenv(override=True)


class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        rmse = metrics.root_mean_squared_error(actual,pred)
        mae = metrics.mean_absolute_error(actual,pred)
        r2 = metrics.r2_score(actual,pred)

        return rmse,mae,r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            # Evaluate metrics
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(Path=self.config.metric_filename, data=scores)

            # Log parameters and metrics to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            
            if tracking_url_type_store !="file":
                mlflow.sklearn.log_model(model,'model',registered_model_name='ElasticNetModel')
            else:
                mlflow.sklearn.log_model(model,'model')

                  
