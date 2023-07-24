import os
from dotenv import load_dotenv
from CreditCardFraud.utils.common import upload_files_to_mongodb
from pathlib import Path
import pandas as pd

load_dotenv()

mongo_client_url = os.getenv('pymongo_url')
filepath = str(Path(os.path.join('research\data','data.csv')))

if __name__ == '__main__':    
    upload_files_to_mongodb(mongo_client_url,'CreditCardFraud',filepath)




