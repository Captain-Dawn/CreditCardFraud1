from CreditCardFraud.config.configuration import ConfigurationManager
from CreditCardFraud.components.data_validation import DataValidation
from CreditCardFraud.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
        logger.info("DataValidationTrainingPipeline completed successfully")