# importing some liabrarires to download filw from git
import os
import urllib.request as request
import requests
from src.DataScience import logger
import zipfile
from src.DataScience.entity.config_entity import DataIngestionConfig

# Data Ingestion component
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        # first lets check if the file is already downloaded
        if not os.path.exists(self.config.local_data_file):
            # Here i am downloading the file from the source URL and saving it to the local data file
            # response = requests.get(self.config.source_URL,stream=True)

            # with open(self.config.local_data_file, 'wb') as file:
            #     for chunk in response.iter_content(chunk_size=8192):
            #         file.write(chunk)
            filename,_ = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Data downloaded at {filename}")
        else:
            logger.info("Data already exists")

    # After download we have to retrive the data
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            