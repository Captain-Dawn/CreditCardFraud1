import os
import pandas as pd
from sklearn.ensemble import  RandomForestClassifier
import joblib
from sklearn.metrics import  accuracy_score , classification_report
from CreditCardFraud.logging import logger
from CreditCardFraud.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        target_column = train_data.columns[-1]

        train_x = train_data.drop([target_column], axis=1)
        test_x = test_data.drop([target_column], axis=1)
        train_y = train_data[target_column]
        test_y = test_data[target_column]

        model = RandomForestClassifier(criterion=self.config.criterion, max_features=self.config.max_features,
                                       n_estimators=self.config.n_estimators, random_state=42)
        model.fit(train_x, train_y)

        y_pred = model.predict(test_x)

        accuracy = accuracy_score(test_y, y_pred)
        cr = classification_report(test_y, y_pred)

        logger.info(f"""The accuracy of {model} is {accuracy} \n\n
        classification report is {cr}""")

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))