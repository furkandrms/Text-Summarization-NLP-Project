from textSummarize.config.configuration import ConfigurationManager
from textSummarize.conponents.data_transformation import DataTransformation
from textSummarize.logging import logger 


class DataTransformationTrainPipeline: 
    def __init__(self):
        pass

    
    def main(self): 
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()




