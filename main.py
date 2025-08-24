from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.DataIngestionPipeline import DataIngestionTrainingPipeline
from src.DataScienceProject.pipeline.DataValidationPipeline import DataValidationTrainingPipeline
from src.DataScienceProject.pipeline.DataTransformationPipeline import DataTransformationPipeline
from src.DataScienceProject.pipeline.DataTransformationPipeline import DataTransformationPipeline
from src.DataScienceProject.pipeline.ModelTrainerPipeline import ModelTrainerPipeline
from src.DataScienceProject.pipeline.ModelEvaluationPipeline import ModelEvaluationPipeline



STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started >>>>>')
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f'>>>>> stage {STAGE_NAME} completed >>>>>')
except Exception as e:
    logger.exception(e)
    raise e

logger.info('Alhumdullillah sb okay h boss!')

STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started >>>>>')
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f'>>>>> stage {STAGE_NAME} completed >>>>>')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started >>>>>')
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f'>>>>> stage {STAGE_NAME} completed >>>>>')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started >>>>>')
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer_pipeline()
    logger.info(f'>>>>> stage {STAGE_NAME} completed >>>>>')
except Exception as e:
    logger.exception(e)
    raise e

    
STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started >>>>>')
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation_pipeline()
    logger.info(f'>>>>> stage {STAGE_NAME} completed >>>>>')
except Exception as e:
    logger.exception(e)
    raise e

