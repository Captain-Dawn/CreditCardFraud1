import os
from CreditCardFraud.logging import logger
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import joblib
from CreditCardFraud.entity import DataTransformationConfig
from pathlib import Path


class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train , test = train_test_split(data, random_state=0)
        return train , test
    
    def transforming(self,train,test):
        target = 'default payment next month'
        X_train = train.drop(target,axis=1)
        y_train = train[target]
        X_test = test.drop(target,axis=1)
        y_test = test[target]

        numerical_cols = X_train.columns
        
        numerical_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
        
        preprocessor = ColumnTransformer([
                ('numerical_pipeline',numerical_pipeline , numerical_cols)
            ])
        
        X_train_arr = preprocessor.fit_transform(X_train)
        X_test_arr = preprocessor.transform(X_test)

        train_data = pd.DataFrame(np.c_[X_train_arr,y_train],columns=train.columns)
        test_data = pd.DataFrame(np.c_[X_test_arr,y_test],columns=test.columns)
    
        train_data.to_csv(os.path.join(self.config.root_dir , "train.csv"),index=False)
        test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False)    



        logger.info("Data Transformation Completed")

        logger.info(f"""The shape of the training data is {train_data.shape},
                    the shape of the testing data is {test_data.shape}""")
        preprocessor_path = Path(os.path.join(self.config.root_dir, "preprocessor.joblib"))
        joblib.dump(value=preprocessor ,filename = preprocessor_path)
        logger.info(f"The preprocessor was saved at {preprocessor_path}")