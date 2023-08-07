import os
from box.exceptions import BoxValueError
import yaml
from CreditCardFraud.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from database_connect import mongo_operation as mongo
import pandas as pd
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns ConfigBox

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories to create
        ignore_log (bool, optional): ignore if multiple directories is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"creating directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB

    Args:
        path (Path): Path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"


@ensure_annotations
def upload_files_to_mongodb(mongo_client_con_string:str,collection_name:str,filepath:str,database_name="demoDB"):
    """takes the path of a csv file , reads the data ,
    generates a dataframe and dumps in the mongo database with
    the desired collection name and default database name=demoDB

    Args:
        mongo_client_con_string (str): client connection string
        collection_name (str): collection name
        filepath (str): path to the csv file
        database_name (str, optional): name of the database. Defaults to "demoDB".
    """
    mongo_connection = mongo(
        client_url = mongo_client_con_string,
        database_name= database_name,
        collection_name= collection_name,
    )


    mongo_connection.bulk_insert(filepath)
    
    logger.info(f"{collection_name} dataset is uploaded to mongodb")
    print(f"{collection_name} dataset is uploaded to mongodb")