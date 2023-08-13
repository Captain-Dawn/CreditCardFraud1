from CreditCardFraud.config.configuration import ConfigurationManager
from CreditCardFraud.components.model_evaluation import ModelEvaluation
from CreditCardFraud.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        logger.info("Model Evaluation Pipeline completed Successfully")