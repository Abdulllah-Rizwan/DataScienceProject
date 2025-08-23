from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.DataIngestionPipeline import DataIngestionTrainingPipeline



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