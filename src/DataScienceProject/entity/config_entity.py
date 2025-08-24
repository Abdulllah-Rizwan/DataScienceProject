from calendar import day_abbr
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass 
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_filename: Path
    target_column: str
    mlflow_uri: str

