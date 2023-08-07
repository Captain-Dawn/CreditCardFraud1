from CreditCardFraud.config.configuration import ConfigurationManager
from CreditCardFraud.components.data_transformation import DataTransformation
from CreditCardFraud.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        train , test = data_transformation.train_test_splitting()
        data_transformation.transforming(train=train ,test=test)
        logger.info("DataTransformationTrainingPipeline completed successfully")