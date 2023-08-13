import os
import pandas as pd
from sklearn.metrics import accuracy_score , roc_auc_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from CreditCardFraud.utils.common import save_json
from CreditCardFraud.logging import logger
from pathlib import Path
from CreditCardFraud.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        accuracy = accuracy_score(actual,pred)
        roc_auc = roc_auc_score(actual,pred)
        return accuracy , roc_auc
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualitites = model.predict(test_x)

            (accuracy , roc_auc) = self.eval_metrics(test_y , predicted_qualitites)

            # Saving metrics as local
            scores = {"accuracy score":accuracy, "roc auc score":roc_auc}
            save_json(path = Path(self.config.metric_file_name),data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('accuracy score',accuracy)
            mlflow.log_metric('roc auc score',roc_auc)

            # Model registry does not work with file store
            if tracking_uri_type_store != 'file':

                # Register the model
                # There are other ways to use the model registry , which depends on the use case
                # Please refer to the documentation for more information
                # https://mlflow.org/docs/latest/model-registry.html #api-workflow
                mlflow.sklearn.log_model(model,'model' , registered_model_name="RandomForestClassifier")

            else:
                mlflow.sklearn.log_model(model,'model')
            
            logger.info(f"model evaluated with following parameter {self.config.all_params} and mlflow updated with following scores {scores}")