import os
import yaml
from src.DataScienceProject import logger
import json
import joblib ## Pickle file alternative
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import  BoxValueError



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Yaml file: {path_to_yaml} is loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Yaml file is empty.')
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool ):
    try: 
        for path_to_directory in path_to_directories:
            os.makedirs(path_to_directory,exist_ok=True) 
            if verbose:
                logger.info(f'Directory created at {path_to_directory}')
    except Exception as e:
        logger.exception(e)
        raise e

@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path,'w') as f:
            json.dump(data,f,indent=4)
        
        logger.info(f'Data is saved as json succesfully at: {Path}')
    except Exception as e:
        logger.exception(e)
        raise e

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    try:
        with open(path,'r') as f:
            data = json.load(f)

        logger.log(f'Data is loaded as json successfully')    
        return ConfigBox(data)
    except Exception as e:
        logger.exception(e)
        raise e

@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data,filename=path)
        logger.info(f'Model is saved at {path}')
    except Exception as e:
        logger.exception(e)
        raise e

@ensure_annotations
def load_bin(path:Path):
    try:
        data = joblib.load(path)
        logger.info(f'Model fetched from: {path}')
        return data
    except Exception as e:
        logger.exception(e)
        raise e