from tabnanny import verbose
from src.DataScienceProject.utils.common import create_directories, read_yaml
from src.DataScienceProject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from src.DataScienceProject.constants import *
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root],verbose=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir],verbose=True)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir],verbose=True)

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_dir,
            all_schema=schema
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir],verbose=True)

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        

        create_directories([config.root_dir],verbose=True)
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_path = config.train_data_path,
            test_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name

        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir],verbose=True)

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            test_data_path = config.test_data_path,
            all_params = params,
            metric_filename = config.metric_filename,
            mlflow_uri = os.getenv('MLFLOW_TRACKING_URI'),
            target_column = schema.name
        )

        return model_evaluation_config