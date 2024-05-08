from textSummarize.config.configuration import ConfigurationManager
from textSummarize.conponents.data_ingestion import DataIngestion
from textSummarize.logging import logger 


class DataIngestionTrainPipeline: 
    def __init__(self) -> None:
        pass

    def main(self): 
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()