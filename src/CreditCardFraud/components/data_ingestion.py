import os
from CreditCardFraud.logging import logger
from CreditCardFraud.utils.common import get_size
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
from CreditCardFraud.entity import DataIngestionConfig
from pathlib import Path



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            load_dotenv()
            filename = self.config.local_data_file
            mongo_client_con_string =  os.getenv("pymongo_url")
            database_name ='demoDB'
            collection_name = 'CreditCardFraud'

            myclient = MongoClient(mongo_client_con_string)
            mydb = myclient[database_name]
            mycol = mydb[collection_name]


            mongo_docs = list(mycol.find())
            data = pd.DataFrame(mongo_docs)
            data.sort_values('_id').reset_index(drop=True).iloc[:,1:].to_csv(filename,index=False)
            logger.info(f"{filename} downloaded!")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")