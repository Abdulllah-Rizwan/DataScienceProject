from src.DataScienceProject import logger
from src.DataScienceProject.components.model_evaluation import ModelEvaluation
from src.DataScienceProject.config.configuration import ConfigurationManager

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation_pipeline(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e