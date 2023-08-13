from CreditCardFraud.constants import *
from CreditCardFraud.utils.common import read_yaml , create_directories
from CreditCardFraud.entity import (DataIngestionConfig,
                                    DataValidationConfig,
                                    DataTransformationConfig,
                                    ModelTrainerConfig,
                                    ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file= config.local_data_file
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    
    def get_data_transformation_config(self) ->  DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestClassifier

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            criterion=params.criterion,
            max_features=params.max_features,
            n_estimators=params.n_estimators
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForestClassifier

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params= params,
            metric_file_name=config.metric_file_name,
            target_column="default payment next month",
            mlflow_uri="https://dagshub.com/tejas05in/CreditCardFraud1.mlflow"
        )
        return model_evaluation_config