from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.DataIngestionPipeline import DataIngestionTrainingPipeline
from src.DataScienceProject.pipeline.DataValidationPipeline import DataValidationTrainingPipeline



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