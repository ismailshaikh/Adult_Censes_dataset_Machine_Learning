
from income_census.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from income_census.exception import IC_Exception
from income_census.util.util import read_yaml_file
from income_census.logger import logging
import os,sys
from income_census.constant import *


# config_entity.py + config.yaml is used

class Configuration:
    
    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH, 
        current_time_stamp:str = CURRENT_TIME_STAMP) -> None:
        
        try:

            self.config_info  = read_yaml_file(file_path=config_file_path)

            self.training_pipeline_config = self.get_training_pipeline_config()

            self.time_stamp = current_time_stamp

        except Exception as e:
            raise IC_Exception(e,sys) from e



    def get_data_ingestion_config(self)->DataIngestionConfig:
        """
        data_ingestion_artifact_dir  -> (artifact/Data_Ingestion/Time_Stamp)
        raw_data_dir = (data_ingestion_artifact_dir/raw_dir)
        ingested_data = (data_ingestion_artifact_dir/ingested_data)
        train = (ingested_data/train)
        test = (ingested_data/test)
        """

        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            # Artifact directory path created (income_census//artifact//Data_ingestion//Time stamp)
            data_ingestion_artifact_dir = os.path.join(
                                artifact_dir,
                                DATA_INGESTION_ARTIFACT_DIR,
                                self.time_stamp
            )
            
            # Dataset download url
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            
            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,
                                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            
            ingested_train_dir = os.path.join(
                                ingested_data_dir,
                                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            
            ingested_test_dir = os.path.join(
                                ingested_data_dir,
                                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )
        
            
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url = dataset_download_url,
                ingested_train_dir = ingested_train_dir,
                ingested_test_dir = ingested_test_dir
            )
            logging.info(f"Data Ingestion Config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    
    
    def get_data_validation_config(self)->DataValidationConfig:
        try:
            
            data_validation_config = DataValidationConfig(
                schema_file_path = schema_file_path,
            )
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            pass
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    def get_model_trainer_config(self)->ModelTrainerConfig:
        try:
            pass
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        try:
            pass
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    
    def get_model_pusher_config(self)->ModelPusherConfig:
        try:
            pass
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

            artifact_dir = os.path.join(ROOT_DIR,
                            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            
            logging.info(f"Training Pipeline Config: {training_pipeline_config}")
            return training_pipeline_config
        
        except Exception as e:
            raise IC_Exception(e,sys) from e
    
    
    