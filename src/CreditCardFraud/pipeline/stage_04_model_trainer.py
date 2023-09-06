from CreditCardFraud.config.configuration import ConfigurationManager
from CreditCardFraud.components.model_trainer import ModelTrainer
from CreditCardFraud.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        logger.info("Model Trainer Training Pipeline completed Successfully")