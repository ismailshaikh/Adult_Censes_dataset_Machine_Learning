from msilib.schema import Icon
import os,sys
from turtle import down
from income_census.constant import ROOT_DIR
from income_census.exception import IC_Exception
from income_census.logger import logging
from income_census.entity.config_entity import DataIngestionConfig
from income_census.entity.artifact_entity import DataIngestionArtifact
# import opendatasets as od
import shutil
import pandas as pd




class DataIngestion:
    
    def __init__(self):
        try:
            logging.info(f"{'='*20}Data Ingestion log Started. {'='*20} ")
            self.data_ingestion_config = DataIngestionConfig
        except Exception as e:
            raise IC_Exception(e,sys) from e
        
    """
    Steps:
    
    Download ->                         using Kggle api
            od.download("https://www.kaggle.com/datasets/overload10/adult-census-dataset")
            
            # reading the CSV file
            file = ("adult-census-dataset/adult.csv")
            newData = pd.read_csv(file)
            
    
    Exctract dataset ->                 store in variable or somewhare
    Train-Test-split ->
    Output to Next pipeline component
    
    
    """
        
    def download_income_data(self):
        try:
            # dataset_url = "https://www.kaggle.com/datasets/overload10/adult-census-dataset"
            # data_dir="adult-census-dataset/adult.csv"
            # od.download_kaggle_dataset(dataset_url=dataset_url,data_dir=data_dir,force=True )
            pass
            root_dir = ROOT_DIR
            raw_folder = os.listdir(root_dir)[os.listdir(root_dir).index("Dataset")]
            adult_csv_file = os.listdir(raw_folder)[0]
            source_file_path = os.path.join(raw_folder,adult_csv_file)
            
            download_dir = self.data_ingestion_config.dataset_download_url
            
            os.makedirs(download_dir,exist_ok=True)
            
            destination_file_path = os.path.join(download_dir, adult_csv_file)
            
            logging.info(f"Moving file from :[{source_file_path}] into :[{destination_file_path}]")
            
            shutil.move(source_file_path, destination_file_path)
            
            logging.info(f"File has been Move successfully.")
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    
    

    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            download_dir = self.data_ingestion_config.dataset_download_url
            
            file_name = os.listdir(download_dir)[0]

            income_file_path = os.path.join(download_dir,file_name)

            logging.info(f"Reading csv file: [{income_file_path}]")
            
            income_data_frame = pd.read_csv(income_file_path)
            
            
            
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise IC_Exception(e,sys) from e