import os 
import yaml
from src.DataScience import logger
import json
import joblib
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from box.exceptions import BoxValueError
from typing import Any

@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """Reads a yaml file and returns a dictionary"""

    try:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)
            logger.info(f"Reading yaml file : {filepath} successfully")
        return ConfigBox(data)
    except BoxValueError:
        raise ValueError(f"Error reading yaml file : {filepath}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(filepaths: list, verbose=True):
    """Creates list of directories if they do not exist"""
    for path in filepaths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(path: Path, data:dict):
    """Saves a dictionary to a json file"""
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    logger.info(f"Saved data to json file : {path}")

@ensure_annotations
def load_json(path: Path, data:dict):
    """loading json file to a dictionary"""
    with open(path, "r") as file:
        content = json.load(path)
    logger.info(f"opening data to json file : {path}")
    return content

@ensure_annotations
def save_model_joblib(data: Any, path:Path):
    """
    Save in binary format using joblib
    
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved model to file : {path}")

@ensure_annotations
def loading_model_joblib(path:Path):
    """
    Save in binary format using joblib
    
    """
    data = joblib.load(path)
    logger.info(f"Loading model to file : {path}")
    return data